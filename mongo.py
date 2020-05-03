from pymongo import MongoClient
from config import DBURL

#String connection
client = MongoClient(DBURL, maxPoolSize=50, connect=False)
print(f"Connected to DBURL")

#Create database 
db = client["API"]

# Create Collections
unique = db['unique']