from fastapi import APIRouter

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

@router.post("/")
def create_order():

    return {
        "order_id": 98765,
        "status": "Order Confirmed"
    }

@router.get("/{order_id}")
def get_order(order_id: int):
    return {
        "order_id": order_id,
        "status": "Shipped"
    }