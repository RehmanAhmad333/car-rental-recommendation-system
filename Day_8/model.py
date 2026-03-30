import pandas as pd  # type: ignore
import numpy as np   # type: ignore
from pathlib import Path
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler   # type: ignore
from sklearn.metrics.pairwise import cosine_similarity    # type: ignore


# Use absolute paths so the module can be imported from any working directory
BASE_DIR = Path(__file__).resolve().parent
orignal_df = pd.read_csv(BASE_DIR / "car_dataset.csv")   # type: ignore
feature_df = pd.read_csv(BASE_DIR / "feature_matrix.csv")   # type: ignore


def recommend(category , max_price , top_car=5):   # type: ignore
    # filter the data from data set what user search 
    filtered = orignal_df[(orignal_df["category"] == category) & (orignal_df["pricePerDay"] <= max_price)]
    # print(f"filtered cars : {filtered} \n\n\n")
    
    # check something find or not
    if filtered.empty:
        return {"message": "No cars found", "car_ids": []}


    # filter cars by id
    filtered_ids = filtered["car_id"].values
    # print(f"Filtered car_ids: {filtered_ids}\n\n\n")

    # filetr car with id from feature_matrix dataset
    filter_feature = feature_df[feature_df["car_id"].isin(filtered_ids)]
    # print(f"Filtered from feature matrix df: {filter_feature}\n\n\n")
    
        
    # selectiong the feature cols
    category_cols = [col for col in feature_df.columns if col not in ['car_id', 'name','pricePerDay', 'price_scaled', 'category']]
    # print("category_cols : " , category_cols)
    
    feature_cols = category_cols + ["price_scaled"]

    # taking the Similarity
    features = filter_feature[feature_cols].values
    # print(f"Taking the features : {features}\n\n\n")

    samilarity = cosine_similarity(features)

    # top n cars 
    first_car_similarity = samilarity[0]

    similar_cars = sorted(enumerate(first_car_similarity) , key=lambda x:x[1] , reverse=True)[1: top_car+1]

    # returen car id

    recommended_ids = []

    for i in similar_cars:
        car_index = i[0]
        car_id = filter_feature.iloc[car_index]["car_id"]
        recommended_ids.append(int(car_id))   # type: ignore

    return{
        "category": category,
        "max_price": max_price,
        "car_ids": recommended_ids
    } # type: ignore
