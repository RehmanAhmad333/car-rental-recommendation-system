from fastapi import FastAPI

from pymongo import MongoClient

import os
from dotenv import load_dotenv

app = FastAPI

# Load env enviorement
load_dotenv()

# Mongo DB
MONGO_DB = os.getenv("DB_URL")
DB_NAME = "car_recommend_db"
COLLECTION_NAME = "cars"

try:
    client = MongoClient(MONGO_DB)
    client.admin.command('ping')
    print("Connection successful!")
    print("Databases:", client.list_database_names())

    db = client(DB_NAME)
    my_collection  = db[COLLECTION_NAME]

except Exception as e:
    print("Connection failed:", e)


# Read data from Data base


