# 阅览室（Reading Room）—— 缮写室的自选文章层

> 缮写室（CK3 Scriptorium）的知识来自 wiki 与游戏 dump 两类**权威**来源；
> 阅览室存放**你自己找到的**好文章——论坛深扒、Reddit 机制帖、性能实测、
> Steam 攻略等知识库未覆盖的洞见。每篇以你自己的话写成笔记，附原文出处。

## 为什么是"笔记"而不是"存档原文"

整篇搬运第三方文章 = 无授权再分发他人版权内容，这是本仓库的许可红线
（见 `LICENSES.md`）。所以本室只收：

- **你写的摘要/笔记**（消化后的内容，版权是你的，随仓库 MIT）；
- **原文出处链接** + 作者 + 发现日期（可追溯）；
- 少量**注明出处的短引用**（加引号并标明来自原文），用于保留关键原文措辞。

## 怎么加一篇文章（三步）

1. 复制 `_template.md` 到 `articles/`，文件名用英文短横线（如
   `on-action-weight-analysis.md`）；
2. 填写头部字段（title / source / author / found / game_version / tags /
   digest——digest 一两句话，会进 catalog 检索目录）；
3. 正文写你自己的笔记；然后同步目录：
   `python scripts\reading_room.py --sync`

`--sync` 会把阅览室条目再生进 `catalog.md` 末尾的标记区块（纯机械生成，
改头部字段后重跑即可）。`--check` 校验格式与目录同步（CI 会跑）。

## 权威级（重要）

| 层 | 权威级 |
|---|---|
| 游戏 dump（`game_docs/script_docs/`） | 最高 |
| wiki 讲解（`pages/`） | 中 |
| **阅览室自选笔记（`reading_room/articles/`）** | **参考级（最低）** |

阅览室内容**不得**作为唯一依据推翻 dump/wiki；冲突时以后者为准并注明。
版本敏感内容记得填 `game_version`（检索时按 catalog 规约配方 D 核对时效）。
