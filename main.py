from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the Product schema
class Product(BaseModel):
    name: str
    price: float
    description: str = None  # Optional

# GET request - Home route
@app.get("/")
async def home():
    return {"message": "This is the home page of the FASTAPI application!"}

# GET request - All products
@app.get("/product")
async def get_all_product():
    return {"message": "Welcome to the FastAPI application with async support!"}

# GET request - Single product by ID
@app.get("/products/{product_id}")
async def single_id(product_id: int):
    return {
        "message": "Welcome to the FastAPI application with async support!",
        "product_id": product_id
    }

# POST request - Create product
@app.post("/product")
async def create_product(product: Product):
    return {
        "response": "Product created successfully",
        "product": product
    }

# PUT request - Update product
@app.put("/product/{product_id}")
async def update_product(product_id: int, product: Product):
    return {
        "response": "Product updated successfully",
        "product_id": product_id,
        "product_name": product.name,
        "product_price": product.price,
        "product_description": product.description
    }
