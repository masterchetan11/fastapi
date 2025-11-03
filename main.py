from fastapi import FastAPI
from models import product

app = FastAPI()

@app.get("/")

def greet():
    return " this is fast api"

products = [
    product(id = 1,name = "laptop",description="dell ",price=45000,quantity=5),
    product(id = 2,name = "phone",description="apple",price=70000,quantity=10), 
]

@app.get("/products")
def _products():
    return products
@app.get("/products/{id}")
def get_products_by_id(id:int):
    for product in products:
        if product.id == id:
            return product
    return "product not found"
@app.post("/products")
def add_product(product:product):
    products.append(product)
    return products 

@app.put("/product")
def update_product(id:int ,product:product):
    for i in range (len(products)):
        if products[0].id ==product:
            return "product added  successfully"
        
    return "product not found"