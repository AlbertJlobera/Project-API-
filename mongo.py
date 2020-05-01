from pymongo import MongoClient
from config import DBURL

#String connection
client = MongoClient(DBURL, maxPoolSize=50, connect=False)
print(f"Connected to DBURL")

#Create database and collections
db = client["Project"]
messages = db["Messages"]
chats = db["Chat"]
users = db["Users"]