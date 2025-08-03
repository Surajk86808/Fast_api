from fastapi import FastAPI, Query
from typing import Annotated
from pydantic import AfterValidator

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI app!"}

PRODUCTS = [
    {"id": 1,
     "name": "Laptop",
     "price": 999.99,
     "description": "A high-performance laptop", "category": "Electronics"},
    {"id": 2, "name": "Smartphone", "price": 599.99, "description": "A latest smartphone", "category": "Electronics"},
    {"id": 3, "name": "Coffee Maker", "price": 49.99, "description": "Programmable coffee maker", "category": "Kitchen"},
    {"id": 4, "name": "Blender", "price": 99.99, "description": "High-speed blender", "category": "Kitchen"},
    {"id": 5, "name": "TV", "price": 799.99, "description": "4K Ultra HD Smart TV", "category": "Electronics"},
]

# ✅ Multi-parameter search using list + validation
@app.get("/products")
async def get_products(
    search: Annotated[
        list[str] | None,
        Query(
            default=None,
            max_length=15,
            pattern="^[a-z]+$",
            description="Search for products by name",
            alias="s",
            deprecated=True
        )
    ]
):
    if search:
        filtered_products = []
        for product in PRODUCTS:
            for search_term in search:
                if search_term.lower() in product["name"].lower():
                    filtered_products.append(product)
                    break
        return filtered_products
    return PRODUCTS

# ✅ Custom validation for product ID
def validate_id(id: int):
    if not str(id).startswith("1"):
        raise ValueError("ID must start with 1")
    return id

@app.get("/products/{id}")
async def get_product(id: Annotated[int, AfterValidator(validate_id)]):
    for product in PRODUCTS:
        if product["id"] == id:
            return product
    return {"error": "Product not found"}
