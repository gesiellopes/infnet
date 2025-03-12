import pandas as pd


from loguru import logger
from pymongo import MongoClient
from sys import stderr

logger.remove()
logger.add(stderr, format="{time:HH:mm:ss} | <lvl>{level} </lvl> {level.icon} | <lvl>{message}</lvl>")


client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['datalake']
collection = db['raw']

df = pd.read_csv('data.csv')

data = df.to_dict(orient='records')
collection.insert_many(data)

logger.success('Data inserted successfully!')
