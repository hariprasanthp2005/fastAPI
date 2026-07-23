from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["Products"])

products = [
    {'pid':101,'product_name':'Marker Pen','price':30,'category':'Stationary'},
    {'pid':102,'product_name':'Lenovo Mouse','price':400,'category':'Electronics'},
    {'pid':103,'product_name':'ThinkPad','price':108000,'category':'Electronics'},
    {'pid':104,'product_name':'Water Bottle','price':10,'category':'Groceries'},
    {'pid':105,'product_name':'Dell Inspiron','price':150000,'category':'Electronics'},
    {'pid':106,'product_name':'Mac Book Pro','price':183000,'category':'Electronics'},
    {'pid':107,'product_name':'Stappler','price':35,'category':'Stationary'},
    {'pid':108,'product_name':'R Pen','price':10,'category':'Stationary'},
    {'pid':109,'product_name':'Parker Pen','price':200,'category':'Stationary'},
    {'pid':110,'product_name':'Meta Rayban','price':40000,'category':'Electronics'}
]

# Get all products or filter by price/category
@router.get("/")
def get_products(price: int | None = None, category: str | None = None):

    result = products

    if price is not None:
        result = [p for p in result if p["price"] <= price]

    if category is not None:
        result = [
            p for p in result
            if p["category"].lower() == category.lower()
        ]

    return result


# Get product by ID
@router.get("/{pid}")
def get_product(pid: int):

    for product in products:
        if product["pid"] == pid:
            return product

    return {"msg": "Product Not Available"}
     