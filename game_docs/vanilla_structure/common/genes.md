# common/genes 结构摘要

- 游戏目录：`F:\SteamLibrary\steamapps\common\Crusader Kings III\game`（CK3 1.20.1；快照日期与指纹见 manifest.json）
- 文件数：12（其中 Jomini 解析 11 个）
- 顶层块条目总数：13，跨文件唯一条目 6
- 本摘要只含结构信息（路径/大小/顶层块名/计数），零原版内容复制。

## 文件清单

| 文件 | 字节 | 顶层块 | 标量键 | 解析 |
|---|---|---|---|---|
| `00_genes_color.txt` | 345 | 1 | 0 | jomini |
| `01_genes_morph.txt` | 431579 | 3 | 12 | jomini |
| `02_genes_accessories_misc.txt` | 2976 | 1 | 0 | jomini |
| `03_genes_special_accessories_hairstyles.txt` | 49066 | 1 | 0 | jomini |
| `04_genes_special_accessories_beards.txt` | 20895 | 1 | 0 | jomini |
| `05_genes_special_accessories_clothes.txt` | 108659 | 1 | 0 | jomini |
| `06_genes_special_accessories_headgear.txt` | 98313 | 1 | 0 | jomini |
| `07_genes_special_accessories_misc.txt` | 63224 | 1 | 0 | jomini |
| `08_genes_special_visual_traits.txt` | 34009 | 1 | 0 | jomini |
| `09_genes_special_makeup.txt` | 8097 | 1 | 0 | jomini |
| `10_genes_special_misc.txt` | 7031 | 1 | 0 | jomini |
| `_genes.info` | 1052 | - | - | 纯文档（非 Jomini） |

## 条目名 → 定义文件

（查单条定义文件可直接 grep 全局映射：`entry_map.tsv` 首列即条目名；本文件按源文件分节列全量条目名。）

### 00_genes_color.txt（1 条目）

- color_genes

### 01_genes_morph.txt（3 条目）

- age_presets
- decal_atlases
- morph_genes

### 02_genes_accessories_misc.txt（1 条目）

- accessory_genes

### 03_genes_special_accessories_hairstyles.txt（1 条目）

- special_genes

### 04_genes_special_accessories_beards.txt（1 条目）

- special_genes

### 05_genes_special_accessories_clothes.txt（1 条目）

- special_genes

### 06_genes_special_accessories_headgear.txt（1 条目）

- special_genes

### 07_genes_special_accessories_misc.txt（1 条目）

- special_genes

### 08_genes_special_visual_traits.txt（1 条目）

- special_genes

### 09_genes_special_makeup.txt（1 条目）

- special_genes

### 10_genes_special_misc.txt（1 条目）

- special_genes

### 未解析文件

- `_genes.info` — 纯文档（非 Jomini）
