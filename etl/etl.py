import pandas as pd
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['datalake']
collection = db['raw']

df = pd.read_csv('data.csv')

data = df.to_dict(orient='records')
collection.insert_many(data)

print('Data inserted successfully')
