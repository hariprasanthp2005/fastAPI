from fastapi import FastAPI
app=FastAPI()

from routes.product_router import router 

products=[
    {'pid':101,'pname':'Marker Pen','price':30,'category':'Stationary'},
    {'pid':102,'pname':'Lenovo Mouse','price':300,'category':'Electronics'},
    {'pid':103,'pname':'Color Pen','price':10,'category':'Stationary'},
    {'pid':104,'pname':'Think Pad','price':800000,'category':'Electronics'},
    {'pid':105,'pname':'Mobile Phone','price':25000,'category':'Electronics'},
    {'pid':106,'pname':'Mobile Cover','price':250,'category':'Electronics'}
]

'''
Usage:Application Root Request
RestAPI URL: http://127.0.0.1:8000/
Method Type:GET
Required Fields:None
Access Type:Public
'''
@app.get("/")
def root_req():
    return {"msg":"Application Root Request"}

app.include_router(router)







