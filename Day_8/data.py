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
    client = MongoClient(uri)
    # client.admin.command('ping')
    print("Connection successful!")
except Exception as e:
    print("Connection failed:", e)

# db = client[""]          # DB name
# collection = db[""]  # collection name

# all_docs = collection.find({})
# for doc in all_docs:
#     print(doc)



@app.get("/data")
def datafile():
    return {"message": "Hello"}
    