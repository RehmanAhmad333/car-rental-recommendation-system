from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from model import recommend, category_names   

app = FastAPI(
    title="AI car recommendation API",
    description="An API that recommends cars based on user preferences using AI.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to AI Car Recommendation System!",
        "available_categories": category_names   
    }

@app.get("/recommendation")
def get_recommendation(
    category: str = Query(..., description="Car category"),
    max_price: float = Query(..., description="Maximum price per day"),
    top_car: int = Query(5, description="Number of recommendations")
):
    try:
        if category not in category_names:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid category! Choose from: {category_names}"
            )

        if max_price <= 0:
            raise HTTPException(
                status_code=400,
                detail="Price must be greater than 0!"
            )

        result = recommend(category, max_price, top_car)
        return result

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))