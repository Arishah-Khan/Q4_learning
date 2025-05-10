from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/products/")
async def search_products(
    category: str | None = Query(
        None,  
        title="Product Category",
        description="Category for filtering products"
    ),
    price: float | None = Query(
        None,
        title="Price Range",
        description="Price range for filtering products",
        ge=0  
    ),
    rating: int = Query(
        1,  
        title="Product Rating",
        description="Minimum rating for filtering products",
        ge=1, 
        le=5  
    )
):
    return {
        "category": category,
        "price": price,
        "rating": rating
    }
