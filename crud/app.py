from fastapi import FastAPI
from routes.emp_router import router as emp_router
app=FastAPI()

'''
Usage:Application Root
Rest API URL: http://127.0.0.1:8000/
Method Type:GET
Required Fields:None
Access Type:public
'''
@app.get("/")
def root_request():
    return {"msg":"apllication root required"}

app.include_router(emp_router)