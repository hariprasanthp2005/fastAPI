from fastapi import APIRouter

router = APIRouter(prefix="/products")

products = [
    {"id": 101, "name": "HP Victus", "brand": "HP", "category": "Laptop"},
    {"id": 102, "name": "Dell Inspiron", "brand": "dell", "category": "Laptop"},
    {"id": 103, "name": "iPhone 16", "brand": "Apple", "category": "Mobile"},
]
@router.get("/")
def get_products(category: str):
    return [
        p for p in products
        if p["category"].lower() == category.lower()
    ]


@router.get("/read")
def get_product(category: str | None = None):
    print(category)
    if category is None:
        return products

    return [
        p for p in products
        if p["category"].lower() == category.lower()
    ]

@router.get("/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product

    return {"message": "Product not found"}



