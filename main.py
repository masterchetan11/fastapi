from fastapi import FastAPI
from models import product

app = FastAPI()

@app.get("/")

def greet():
    return " this is fast api"

products = [
    product(name="laptop",description="dell ",price=45000,quantity=5),
    product(name="phone",description="apple",price=70000,quantity=10), 
]

@app.get("/products")
def _products():
    return products
