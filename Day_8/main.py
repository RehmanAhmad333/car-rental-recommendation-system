from fastapi import FastAPI , HTTPException , Query    # type: ignore
from fastapi.middleware.cors import CORSMiddleware    # type: ignore
from .model import recommend   # type: ignore
from pathlib import Path

from pydantic import BaseModel
from typing import List

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
    try:
        return {"message": "Welcome to the AI car recommendation system.Server is up and running!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/recommendation")
def get_recommendation(
    category: str = Query(...,description="The category of the car (e.g., SUV, sedan, etc.)"), 
    max_price: float = Query(...,description="The maximum price per day for the car rental."), 
    top_car: int = Query(5,description="The number of top recommended cars to return.")
):
    try:
        # check valid category
        valid_categories = ["SUV", "Electric", 
                        "Luxury", "2-Seater"]
    
        if category not in valid_categories:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid category! Choose from: {valid_categories}"
            )
        
        # Validate price
        if max_price <= 0:
            raise HTTPException(
                status_code=400,
                detail="Price must be greater than 0!"
            )

        result = recommend(category, max_price, top_car)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


