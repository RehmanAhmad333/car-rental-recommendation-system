# Day 6 - Recommendation Model

## Objective
Build the core recommendation engine that 
suggests similar cars based on 
category and price.

## What I Did
- Built recommend() function
- Filter cars by category and max price
- Calculate cosine similarity
- Return top 5 similar car_ids

## How It Works
1. User sends category + max_price
2. Filter matching cars from original_df
3. Get their features from feature_df
4. Calculate cosine similarity
5. Return top N car_ids

## API Input / Output
Input:
- category = "SUV"
- max_price = 100

Output:
{
  "category": "SUV",
  "max_price": 100,
  "car_ids": [2, 3, 4, 5, 41]
}

## Edge Case Handled
If no cars found:
{
  "message": "No cars found",
  "car_ids": []
}

## Tools Used
- Python
- Pandas
- Scikit-learn (cosine_similarity)
- NumPy
- Pickle