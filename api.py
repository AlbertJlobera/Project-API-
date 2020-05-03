from flask import Flask, request, jsonify
import pymongo
from bson.json_util import dumps
from config import PORT
from mongo import *
from errorHandler import *
from bson.objectid import ObjectId
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download("vader_lexicon")

app=Flask(__name__)


#Create User
@app.route("/create/user/<username>")
@errorHandler
def insertUser(username):
    data = { "Name": username,'Messages':[],'Chats':[]}
    user = db.unique.insert_one(data)
    
    return f'<h1> Welcome {username}! :) </h1>'

#Assign chat to user.
@app.route("/chat/<chatname>/user/<username>")
@errorHandler
def creatChat(chatname,username):
    data = db.unique.find({'Name': username},{'_id':0})
    output= []
    if data.count() == 0:
        raise Error404 (f'<h1>This user is not registered.<h1>')
    else:
        query = db.unique.find({'$and': [{'Name': username},{'Chats': [chatname]}]},{'_id':0})
        if query.count() == 0:
            output =  db.unique.update({'Name': username},{'$set':{'Chats': [chatname]}})
            return f'<h1> Hello, {username} the new chat "{chatname}" is Created!</h1>'
        else:
            return f'<h1>Error: you are already in the chat.</h1>'


#Add message to a chat
@app.route('/chat/<chatname>/user/<username>/message/<message>')
@errorHandler
def findChatName(chatname, username, message):
    if db.unique.count_documents({'Name': username,'Chats': [chatname]}) == 0:
        raise Error404 (f'<h1> This user is not registered.</h1>')
    else:
        db.unique.update({'Name': username},{'$set':{"Messages": [message]}})
        return f'<h1> Thank you for your message! </h1>'


# Get all message from chat_ID
@app.route('/chat/<chatname>/list')
@errorHandler
def chatList(chatname):
    output = []
    if db.unique.count({'Chats': chatname}) == 0:
        raise Error404 (f'<h1> This chat is not registered.</h1>')
    else:
        data = list(db.unique.find({ 'Chats': chatname },{'_id':0,'Messages':1}))
        lista=[]
    for item in data:
        for message, sentence in item.items():
            if sentence != "":
                lista.append(sentence)      
    flat_list = [item for sublist in lista for item in sublist]
    return dumps(flat_list)
    
# Calculating sentiment with `NLTK` sentiment analysis
@app.route('/chat/<chatname>/sentiment')
@errorHandler
def getAnalysts(chatname):
    sia = SentimentIntensityAnalyzer()
    output = []
    sentiment =[]
    if db.unique.count({'Chats': chatname}) == 0:
        raise Error404 (f'<h1> This chat is not registered.</h1>')
    else:
        data = list(db.unique.find({ 'Chats': chatname },{'_id':0,'Messages':1}))
        lista=[]
    for item in data:
        for message, sentence in item.items():
            if sentence != "":
                lista.append(sentence)      
    flat_list = [item for sublist in lista for item in sublist]
    for sentence in flat_list:
        return sia.polarity_scores(sentence)
        
        
        

app.run("0.0.0.0", PORT, debug=True)


 