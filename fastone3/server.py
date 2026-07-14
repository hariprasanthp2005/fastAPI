from fastapi import FastAPI

app=FastAPI()


users=[
    1: {"uid":101,"uname":"hp","Avail":True,"discount":None},
    2: {"uid":102,"uname":"vk","Avail":False,"discount":None},
    3: {"uid":103,"uname":"cheeku","Avail":True,"discount":None},
    4: {"uid":104,"uname":"abd","Avail":True,"discount":None},
]

'''
Usage: Application Root Request
Rest API URL: http://127.0.0.1:8000/
Method Type:GET
Required Fields: None 
Acccess Type:Public
'''
@app.get("/")
def root_req():
    return{"msg":"application root request"}

'''
Usage: Application Root Request
Rest API URL: http://127.0.0.1:8000/
Method Type:GET
Required Fields: None 
Acccess Type:Public
'''
@app.get("/users/read")
def fetch_user():
    return users

