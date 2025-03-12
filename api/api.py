import json

from bson.json_util import dumps
from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

client = MongoClient('mongodb://mongodb:27017/')
db = client['datalake']
collection = db['raw']

@app.get("/api")
async def get_data():
    
    data = list(collection.find({}, {"_id": 0}))

    return json.loads(dumps(data))


