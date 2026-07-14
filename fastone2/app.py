from fastapi import FastAPI
app=FastAPI()

'''
Usage: Application Root Request
Rest API URL: http://127.0.0.1:8000/
Method Type:GET
Required Fields: None 
Acccess Type:Public
'''
@app.get("/")
def root_request():
    return{"msg":True}

'''
Usage: Application Root Request
Rest API URL: http://127.0.0.1:8000/
Method Type:POST
Required Fields: None 
Acccess Type:Public
'''
@app.post("/create")
def create_user():
    return{"msg":"new user created successfully"}

'''
Usage: Application Root Request
Rest API URL: http://127.0.0.1:8000/
Method Type:GET
Required Fields: None 
Acccess Type:Public
'''
@app.get("/get")
def get_user():
    return{"msg":"get user"}

'''
Usage: Application Root Request
Rest API URL: http://127.0.0.1:8000/
Method Type:PUT
Required Fields: None 
Acccess Type:Public
'''
@app.put("/update")
def update_user():
    return{"msg":"user updated successfully"}

'''
Usage: Application Root Request
Rest API URL: http://127.0.0.1:8000/
Method Type:DELETE
Required Fields: None 
Acccess Type:Public
'''
@app.delete("/delete")
def update_user():
    return{"msg":"deleted  successfully"}

