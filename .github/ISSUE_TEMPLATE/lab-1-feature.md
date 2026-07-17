---
name: "Lab 1: Product search"
about: Improve this issue, then assign it to Copilot coding agent
title: "Add product search"
labels: ["lab-1", "enhancement"]
assignees: []
---

讓使用者可以透過 `GET /products` 依關鍵字搜尋產品，並且能搭配排序與分頁快速找到想要的商品。

## Scope

- 僅調整 `GET /products`
- 既有的 `GET /products/{product_id}` 行為不得改變
- Response shape 必須維持既有的 `items`、`total`、`page`、`page_size`

## API behavior

`GET /products` 接受以下 optional query parameters：

| Parameter | 規則 |
| --- | --- |
| `q` | 對產品名稱或分類執行不區分大小寫的 partial match |
| `sort` | 僅允許 `name` 或 `price`；無效值回傳 HTTP 422 |
| `order` | 僅允許 `asc` 或 `desc`；預設 `asc`；無效值回傳 HTTP 422 |
| `page` | 大於或等於 1 的整數；預設 `1` |
| `page_size` | `1` 到 `20` 的整數；預設 `20` |

搜尋、排序與分頁必須能組合使用。`total` 代表分頁前的符合筆數。

## Error behavior

- `sort` 或 `order` 傳入不允許的值時回傳 HTTP 422
- `page` 小於 `1` 時回傳 HTTP 422
- `page_size` 不在 `1` 到 `20` 範圍內時回傳 HTTP 422

## Validation

```bash
python scripts/validate.py
pytest -q -m lab1
```

## Acceptance criteria

- [ ] `GET /products?q=<term>` 會對產品名稱或分類執行不區分大小寫的 partial match
- [ ] `GET /products?sort=name` 與 `GET /products?sort=price` 會依指定欄位排序
- [ ] `order` 預設為 `asc`，並支援 `desc`
- [ ] `sort` 或 `order` 的無效值會回傳 HTTP 422
- [ ] `page` 預設為 `1`，且只接受大於或等於 `1` 的整數
- [ ] `page_size` 預設為 `20`，且只接受 `1` 到 `20` 的整數
- [ ] Response 維持既有的 `items`、`total`、`page`、`page_size` shape
- [ ] `total` 回傳分頁前的符合筆數，而不是分頁後的筆數
- [ ] 搜尋、排序與分頁可以同時使用且結果正確
- [ ] `GET /products/{product_id}` 的既有行為不變
- [ ] `python scripts/validate.py` 通過
- [ ] `pytest -q -m lab1` 通過
