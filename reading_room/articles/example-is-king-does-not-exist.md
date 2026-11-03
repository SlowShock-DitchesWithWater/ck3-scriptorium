---
title: is_king 不存在——判定"国王级角色"用 highest_held_title_tier
source: 个人笔记（依据：本仓库 game_docs/script_docs/triggers.md 实测核对）
author: 缮写室维护者
found: 2026-10-23
game_version: 1.20.1
tags: trigger, title-tier, anti-hallucination
digest: 想写"对方是国王"的判定时，is_king 这个 trigger 不存在（模型常见幻觉）；正确写法是 highest_held_title_tier = kingdom（或 >= kingdom 连皇帝一起算），已在 dump 层核实。
---

## 契机

给 AI agent 出的测试题："出生时如果父亲是国王，给孩子加特质与金钱"。
测试代理第一反应想用 `is_king`——在 `game_docs/script_docs/triggers.md`
里 grep 无命中，**这个 trigger 不存在**，属于典型的"看起来像 CK3 语法"的
幻觉词。

## 正确写法（已对照 dump 层核实，1.20.1）

```
father = { highest_held_title_tier = kingdom }
```

- `highest_held_title_tier` 支持 `= / >= / <= / > / < / !=` 比较；
- 要"国王或皇帝都算"：`highest_held_title_tier >= kingdom`；
- 比较符能力来自 dump 条目原文，不是猜测。

## 附带发现

- 父亲若已死且头衔已传，判定自然不成立——写"父亲是国王"类逻辑时要
  想清楚语义边界；
- 法律父亲与生父是两条链（`father` / on_action 侧另有 `on_birth_real_father`），
  按需求选择。

## 教训（对写 mod 的 agent 通用）

任何"想当然存在"的短 trigger/effect 名，先
`grep "### 词名" game_docs/script_docs/triggers.md` 核实再写——短词
（is_/has_/add_ 前缀家族）是幻觉重灾区。
