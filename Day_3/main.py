from fastapi import FastAPI

from pymongo import MongoClient

import os
from dotenv import load_dotenv

from .data import cars

import pandas as pd

app = FastAPI

# Load env enviorement
load_dotenv()

# Mongo DB
MONGO_DB = os.getenv("DB_URL")
DB_NAME = "ai_car_recommendation_system"
COLLECTION_NAME = "cars"

try:
    client = MongoClient(MONGO_DB)
    print("Connection successful!")
    print("Databases:", client.list_database_names())

    db = client[DB_NAME]
    my_collection  = db[COLLECTION_NAME]

except Exception as e:
    print("Connection failed:", e)


# insert data into database 

result = my_collection.insert_many(cars)
print("Data inserted with ID:", result.inserted_ids)


# Retrieve all documents as a list of dictionaries
data = list(my_collection.find())

# Convert to DataFrame
df = pd.DataFrame(data)

print(df.head())







