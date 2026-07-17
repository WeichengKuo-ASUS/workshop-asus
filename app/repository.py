from typing import Literal

from app.models import Product

PRODUCTS = [
    Product(id=1, name="Zenbook 14 OLED", category="Laptop", price=42900),
    Product(id=2, name="ROG Zephyrus G14", category="Gaming Laptop", price=62900),
    Product(id=3, name="ProArt P16", category="Creator Laptop", price=79900),
    Product(id=4, name="TUF Gaming A15", category="Gaming Laptop", price=38900),
    Product(id=5, name="ROG Ally X", category="Handheld", price=26900),
    Product(id=6, name="ProArt Display PA279CRV", category="Monitor", price=15900),
]


def list_products(
    *,
    q: str | None = None,
    sort: Literal["name", "price"] | None = None,
    order: Literal["asc", "desc"] = "asc",
    page: int = 1,
    page_size: int = 20,
) -> tuple[list[Product], int]:
    filtered_products = PRODUCTS.copy()

    if q is not None:
        query = q.casefold()
        filtered_products = [
            product
            for product in filtered_products
            if query in product.name.casefold() or query in product.category.casefold()
        ]

    if sort is not None:
        filtered_products = sorted(
            filtered_products,
            key=lambda product: getattr(product, sort),
            reverse=order == "desc",
        )

    total = len(filtered_products)
    start = (page - 1) * page_size
    end = start + page_size
    return filtered_products[start:end], total


def get_product(product_id: int) -> Product | None:
    return next((product for product in PRODUCTS if product.id == product_id), None)
