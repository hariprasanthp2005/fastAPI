from fastapi import FastAPI

from routers.users import router as user_router
from routers.products import router as product_router
from routers.orders import router as order_router

app = FastAPI(
    title="ShopKart API"
)

app.include_router(user_router)
app.include_router(product_router)
app.include_router(order_router)