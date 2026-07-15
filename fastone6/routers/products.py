from fastapi import APIRouter

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get("/")
def get_products():
    return [
        {
            "id": 1,
            "name": "iPhone 17",
            "price": 95000
        },
        {
            "id": 2,
            "name": "MacBook Air",
            "price": 120000
        }
    ]

@router.get("/{product_id}")
def get_product(product_id: int):
    return {
        "product_id": product_id,
        "stock": 45
    }