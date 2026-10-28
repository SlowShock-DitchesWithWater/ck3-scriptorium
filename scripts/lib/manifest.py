# -*- coding: utf-8 -*-
"""manifest.json 的原子读改写助手。

为什么必须走这里：后续工单会有多个 agent/进程并行抓取并登记 manifest，
直接 read→modify→write 会互相覆盖。本模块提供：
- 文件锁（manifest.json.lock，O_CREAT|O_EXCL 原子创建 + 重试 + 过期锁抢占）
- 原子写（同目录临时文件 + os.replace，读者永远不会看到半截 JSON）

对外主接口：
- read_manifest() -> dict                       读取（无锁，只读永远安全）
- update_page(title, mutate: (entry)->new_entry) 读改写一条页面记录（加锁+原子写）
- with manifest_locked(): ...                    需要多条连续改动时手动持锁
"""
import contextlib
import json
import os
import sys
import time
from typing import Callable, Iterator

from . import config

LOCK_TIMEOUT_SECONDS = 30.0     # 获取锁的最长等待
LOCK_STALE_SECONDS = 120.0      # 超过该年龄的锁视为残留（持有者已死），可抢占


def _lock_path() -> os.PathLike:
    return str(config.MANIFEST_PATH) + ".lock"


@contextlib.contextmanager
def manifest_locked() -> Iterator[None]:
    """manifest.json 的简单互斥锁。

    实现：lock 文件用 os.open(O_CREAT|O_EXCL) 原子创建即视为持锁；
    超时前每 0.2s 重试；锁文件年龄超过 LOCK_STALE_SECONDS 视为持有者
    已崩溃，删除后重新竞争。写锁文件内容为 PID 便于排查。
    """
    lock = _lock_path()
    deadline = time.time() + LOCK_TIMEOUT_SECONDS
    fd = None
    while True:
        try:
            fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            break
        except FileExistsError:
            # 检查残留锁：年龄过大则抢占（持有者异常退出的场景）
            try:
                age = time.time() - os.stat(lock).st_mtime
                if age > LOCK_STALE_SECONDS:
                    print(f"[manifest] 抢占过期锁（年龄 {age:.0f}s）",
                          file=sys.stderr)
                    os.unlink(lock)
                    continue
            except OSError:
                pass  # 锁刚好被释放，直接重试
            if time.time() > deadline:
                raise TimeoutError(
                    f"等待 manifest 锁超时（{LOCK_TIMEOUT_SECONDS:.0f}s），"
                    f"锁文件：{lock}")
            time.sleep(0.2)
    try:
        os.write(fd, str(os.getpid()).encode("ascii"))
        yield
    finally:
        os.close(fd)
        with contextlib.suppress(OSError):
            os.unlink(lock)


def _new_manifest() -> dict:
    """manifest 的初始骨架（schema 见 docs/pipeline.md）。"""
    return {"schema_version": 1, "pages": {}}


def read_manifest() -> dict:
    """读取 manifest；不存在或损坏时返回新骨架（损坏会告警但不中断）。"""
    if not config.MANIFEST_PATH.is_file():
        return _new_manifest()
    try:
        data = json.loads(config.MANIFEST_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"[manifest] 警告：manifest 读取失败（{exc}），按空 manifest 处理",
              file=sys.stderr)
        return _new_manifest()
    # 兼容防御：保证顶层结构完整
    data.setdefault("schema_version", 1)
    data.setdefault("pages", {})
    return data


def _atomic_write_json(path, data: dict) -> None:
    """原子写 JSON：同目录临时文件 + fsync + os.replace。

    Windows 上 os.replace 可能因杀软/同步软件（Defender/syncthing）瞬时
    占用目标文件报 PermissionError（工单04 实测）。做指数退避重试——
    原子性不受影响（仍是整文件替换），只是重试同一替换动作。
    """
    tmp = str(path) + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
        f.flush()
        os.fsync(f.fileno())
    for attempt in range(6):  # 0.1+0.2+0.4+0.8+1.6 ≈ 3.1s 总退避
        try:
            os.replace(tmp, path)
            return
        except PermissionError:
            if attempt == 5:
                raise
            time.sleep(0.1 * (2 ** attempt))


def write_manifest(data: dict) -> None:
    """整表原子写（调用方需已持锁或接受竞态；单进程场景可直接用）。"""
    _atomic_write_json(config.MANIFEST_PATH, data)


def update_page(title: str, mutate: Callable[[dict], dict]) -> dict:
    """读改写单页记录的入口（加锁 + 原子写）。

    mutate 收到该页当前 entry（新页时为空 dict），返回新 entry；
    返回值整体替换旧 entry。函数返回更新后的完整 manifest。
    """
    with manifest_locked():
        data = read_manifest()
        entry = data["pages"].get(title, {})
        data["pages"][title] = mutate(entry)
        _atomic_write_json(config.MANIFEST_PATH, data)
    return data
