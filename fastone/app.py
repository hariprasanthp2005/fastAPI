from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def index_page():
    return{"message":"index page"}

@app.get("/login")
def login_page():
    return{"message":"login page"}

@app.get("/contact")
def contact_page():
    return{"message":"contact page"}



