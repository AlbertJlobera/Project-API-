from pymongo import MongoClient
from config import DBURL
from bson.json_util import dumps, loads
from mongo import *
from api import app
from bson.objectid import ObjectId



@app.route('/chat/create/')
def insertchat(chatname):
    query1 = list(chat.find({'Chat': chatname},{'_id':0}))
    inchat1 = chat.insert_one({'Chat':chatname,'users':[],'message':[]})
    chat_id = inchat1.inserted_id
    return dumps([chat_id,{'Chat':chatname}])

    
@app.route('/chat/<chat_id>/adduser/<username>')
def upchat(chat_id,user_id):
    print(list(chat.find({'_id':ObjectId(chat_id)})))
    chat.update({'_id':ObjectId(chat_id)},{'$push':{'users':ObjectId(user_id)}})
    print(chat_id,user_id)
    return dumps({'users':ObjectId(user_id)})