from fastapi import FastAPI

app = FastAPI()

PRODUCT = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 999.99,
        "description": "A high-performance laptop"
    },
    {
        "id": 2,
        "name": "Smartphone",
        "price": 499.99,
        "description": "A latest model smartphone"
    },
    {
        "id": 3,
        "name": "Headphones",  
        "price": 199.99,
        "description": "Noise-cancelling headphones"
    }
]

# GET request - Home route
@app.get("/product")
async def get_all_product():
    return {
        "response":"List of all products",
            "products": PRODUCTS
   } 
