from fastapi import FastAPI
import requests

app = FastAPI()

# Fetch data from API
req_data = requests.get("https://dummyjson.com/products")
data = req_data.json()
data1 = data["products"]


@app.get("/")
def get_user():
    beauty_product = []

    for product in data1:
        if product["category"] == "beauty":
            beauty_product.append(product)

    return beauty_product
        
