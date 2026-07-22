from fastapi import FastAPI

app = FastAPI()
from routes.product_eg import router 

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