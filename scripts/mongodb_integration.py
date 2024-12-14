from pymongo import MongoClient
import pandas as pd

input_file_path = '/Users/a.s.pravieen/Desktop/DE Project/t4/updated_census_data.csv'
df = pd.read_csv(input_file_path)

client = MongoClient('mongodb://localhost:27017/')

db = client['census_data']

data = df.to_dict(orient='records')

collection = db['census']

result = collection.insert_many(data)

print (len(result.inserted_ids))

print(client.list_database_names())
