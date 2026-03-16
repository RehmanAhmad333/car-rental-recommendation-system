from fastapi import FastAPI

from pymongo import MongoClient

import os
from dotenv import load_dotenv

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

# result = my_collection.insert_many(car_data)
# print("Data inserted with ID:", result.inserted_ids)

# Read all data from database
# all_documents_list = list(my_collection.find({}))
# # print("\nAll data as a list:")
# # print(all_documents_list)

# dict = {}

# print("All documents as a list of dictionaries:")
# for doc in all_documents_list:
#     print(doc)


# Retrieve all documents as a list of dictionaries
data = list(my_collection.find())

# Convert to DataFrame
df = pd.DataFrame(data)

print(df.head())







