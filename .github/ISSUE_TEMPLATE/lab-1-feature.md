---
name: "Lab 1: Product search"
about: Improve this issue, then assign it to Copilot coding agent
title: "Add product search"
labels: ["lab-1", "enhancement"]
assignees: []
---

Add search, sorting, and pagination to `GET /products` so users can quickly find products without changing the existing response shape.

## Scope

- Only change `GET /products`
- Keep the existing `GET /products/{product_id}` behavior unchanged
- Preserve the existing response shape: `items`, `total`, `page`, `page_size`

## API behavior

`GET /products` accepts the following optional query parameters:

| Parameter | 規則 |
| --- | --- |
| `q` | Case-insensitive partial match against product name or category |
| `sort` | Only allow `name` or `price`; invalid values must return HTTP 422 |
| `order` | Only allow `asc` or `desc`; default to `asc`; invalid values must return HTTP 422 |
| `page` | Integer greater than or equal to `1`; default `1` |
| `page_size` | Integer from `1` to `20`; default `20` |

Search, sorting, and pagination must work together. `total` must represent the number of matches before pagination is applied.

## Error behavior

- Return HTTP 422 when `sort` or `order` is outside the allowed values
- Return HTTP 422 when `page` is less than `1`
- Return HTTP 422 when `page_size` is outside the range `1` to `20`

## Validation

```bash
python scripts/validate.py
pytest -q -m lab1
```

## Acceptance criteria

- [ ] `GET /products?q=<term>` performs a case-insensitive partial match on product name or category
- [ ] `GET /products?sort=name` and `GET /products?sort=price` sort by the requested field
- [ ] `order` defaults to `asc` and also supports `desc`
- [ ] Invalid `sort` or `order` values return HTTP 422
- [ ] `page` defaults to `1` and only accepts integers greater than or equal to `1`
- [ ] `page_size` defaults to `20` and only accepts integers from `1` to `20`
- [ ] The response keeps the existing `items`, `total`, `page`, and `page_size` shape
- [ ] `total` reports the number of matches before pagination slicing
- [ ] Search, sorting, and pagination can be combined and still produce correct results
- [ ] `GET /products/{product_id}` behavior remains unchanged
- [ ] `python scripts/validate.py` passes
- [ ] `pytest -q -m lab1` passes
