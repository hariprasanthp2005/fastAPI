from fastapi import FastAPI

app=FastAPI()
'''
Usage: products detail
Rest API URL: http://127.0.0.1:8000/
Method Type:GET
Required Fields: None 
Acccess Type:Public
'''
@app.get("/")
def get_product():
    return {"msg":"getting product deatil"}

'''
Usage: Update product by id
Rest API URL: http://127.0.0.1:8000/
Method Type:PUT
Required Fields: None 
Acccess Type:Public
'''
@app.put("/products/update")
def update_product():
    return {"msg":"product update successfully"}
