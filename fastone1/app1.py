from fastapi import FastAPI

app=FastAPI()

'''
Usage: Application Root Request
Rest API URL: http://127.0.0.1:8000/
Method Type:POST
Required Fields: None 
Acccess Type:Public
'''
@app.post("/")
def index_page():
    return {"msg":"Index Page"}

'''
Usage: Application Root Request
Rest API URL: http://127.0.0.1:8000/
Method Type:GET
Required Fields: None 
Acccess Type:Public
'''

@app.get("/")
def login_page():
    return {"msg":"login page"}