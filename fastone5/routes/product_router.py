from fastapi import APIRouter

router=APIRouter(prefix='/product',default="product module APIs")

'''
Usage:fetch product details
Rest API URL: http://127.0.0.1:8000/product/
Method Type:GET
Required Fields:None
Access Type:public
'''

@router.get("/")
def get_product():
    return {"msg":"product Module -geting User Details"}


'''
Usage:create new product
Rest API URL: http://127.0.0.1:8000/product/
Method Type:POST
Required Fields:uid,uname,loc
Access Type:public
'''

@router.post("/")
def create_product():
    return {"msg":"New product Created Successfully"}

'''
Usage:delete product
Rest API URL: http://127.0.0.1:8000/product/
Method Type:PUT
Required Fields:None
Access Type:public
'''
@router.put("/")
def update_product():
    return {"msg":"updated succesfully"}



'''
Usage:delete product
Rest API URL: http://127.0.0.1:8000/product/
Method Type:DELETE
Required Fields:
Access Type:public
'''
@router.delete("/")
def delete_product():
    return {"msg":"product Deleted succesfully"}