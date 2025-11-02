from fastapi import FastAPI
from models import product 

app = FastAPI()

@app.get("/")
def greet():
    return " this is fast api"

products = [
product(1,"laptop","dell laptop",45000,5),
product(2,"phone","iphone",70000,10)
]

@app.get("/products")
def get_products():
    return products

