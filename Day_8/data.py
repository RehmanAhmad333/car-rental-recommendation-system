from fastapi import FastAPI
from pymongo import MongoClient   # type: ignore
import os   # type: ignore
from dotenv import load_dotenv   # type: ignore

load_dotenv()

app = FastAPI()    

# MongoDB
MONGODB_URI = os.getenv("MONGODB_URI")


uri = os.getenv("MONGODB_URI")
print("Using URI:", uri.replace(uri.split('@')[0].split(':')[1], '****'))  # hide password

try:
    client = MongoClient(uri, serverSelectionTimeoutMS=5000)
    client.admin.command('ping')
    print("Connection successful!")

    db = client["test"]
    collection = db["CarSchema"]

except Exception as e:
    print("Connection failed:", e)
    db = None
    collection = None



@app.get("/data")
def datafile():
    if collection is None:
        return {"error": "Database not connected"}
    
    all_docs = list(collection.find({}, {"_id": 0}))
    return {"data": all_docs}