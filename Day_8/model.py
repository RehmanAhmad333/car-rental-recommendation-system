import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity
from pymongo import MongoClient
import certifi
import os
from dotenv import load_dotenv

load_dotenv()


# MongoDB Connection

uri = os.getenv("MONGODB_URI")

try:
    client = MongoClient(
        uri,
        tlsCAFile=certifi.where(),
        serverSelectionTimeoutMS=5000
    )
    client.admin.command('ping')
    print("MongoDB Connected!")
    
    db = client["test"]
    collection = db["cars"]

except Exception as e:
    print("Connection failed:", e)
    client = None
    collection = None

# Load data from MongoDB
def load_data():
    if collection is None:
        print("No DB connection!")
        return None, None
    
    # take data from MongoDB
    data = list(collection.find({}, {"_id": 0}))
    
    if not data:
        print("No data in DB!")
        return None, None
    
    # Make DataFrame
    original_df = pd.DataFrame(data)
    
    # Add car_id for reference
    original_df['car_id'] = range(1, len(original_df) + 1)
    
    print("Data loaded!")
    print("Categories found:", original_df['category'].unique())
    print("Total cars:", len(original_df))
    
    return original_df

 
# Feature Engineering
def build_feature_matrix(original_df):
    
    # Category Encoding Dynamic!
    encoder = OneHotEncoder()
    category_encoded = encoder.fit_transform(original_df[['category']]).toarray()
    
    # Dynamic category names 
    category_names = encoder.categories_[0].tolist()
    print("Category columns:", category_names)
    
    # Price Normalization
    scaler = MinMaxScaler()
    price_scaled = scaler.fit_transform(
        original_df[['pricePerDay']]
    )
    
    # Feature Matrix  
    feature_matrix = np.hstack([
        category_encoded,
        price_scaled
    ])
    
    # Make dataframe for easy handling
    feature_df = pd.DataFrame(
        feature_matrix,
        columns=category_names + ['price_scaled']
    )
    
    feature_df['car_id'] = original_df['car_id'].values
    feature_df['name'] = original_df['name'].values
    
    return feature_df, category_names

# Load data 
original_df = load_data()

if original_df is not None:
    feature_df, category_names = build_feature_matrix(original_df)
    print("Feature matrix ready!")
    print("Feature columns:", feature_df.columns.tolist())
else:
    feature_df = None
    category_names = []


# Recommend Function
def recommend(category, max_price, top_car=5):
    
    if original_df is None or feature_df is None:
        return {
            "message": "Database not connected",
            "car_ids": []
        }
    
    # Filter cars by category and price
    filtered = original_df[
        (original_df['category'] == category) &
        (original_df['pricePerDay'] <= max_price)
    ]
    
    # None check
    if filtered.empty:
        return {
            "message": "No cars found",
            "car_ids": []
        }
    
    # Take filtered car IDs
    filtered_ids = filtered['car_id'].values
    
    # Feature matrix filter
    filter_feature = feature_df[
        feature_df['car_id'].isin(filtered_ids)
    ]
    
    # Dynamic feature cols
    exclude_cols = ['car_id', 'name', 'price_scaled']
    feature_cols = [
        col for col in feature_df.columns
        if col not in exclude_cols
    ]
    
    # Similarity
    features = filter_feature[feature_cols].values
    similarity = cosine_similarity(features)
    
    # Top N
    similar_cars = sorted(
        enumerate(similarity[0]),
        key=lambda x: x[1],
        reverse=True
    )[1:top_car+1]
    
    # IDs return
    recommended_ids = [
        int(filter_feature.iloc[i[0]]['car_id'])
        for i in similar_cars
    ]
    
    return {
        "category": category,
        "max_price": max_price,
        "car_ids": recommended_ids
    }