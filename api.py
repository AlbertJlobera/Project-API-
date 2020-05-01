from flask import Flask, request
import pymongo
from bson.json_util import dumps
from config import PORT
from mongo import *



app=Flask(__name__)




#Create User
@app.route("/user/create/<username>")

def insertUser(username):
    data = { "name": f"{username}"}
    user = users.insert_one(data)
    return dumps(user.inserted_id)

@app.route('/chat/create')

def insertChat(chat):
    data = {'message':[],users:[]}
    chat = collection.insert_one(data)
    return dumps(newchat.insert_id)


"""@app.route('/chat/<chat_id>/addmessage')

def insertRoute():
    data = """


app.run("0.0.0.0", PORT, debug=True)




 # http://0.0.0.0:3500/user/create/Albert