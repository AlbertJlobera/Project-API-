from pymongo import MongoClient
from config import DBURL
from bson.json_util import dumps
from mongo import *
from api import app


#Create User
@app.route("/user/create/<username>")
def insertUser(username):
    data = { "name": f"{username}"}
    user = users.insert_one(data)
    return dumps(user.inserted_id)










