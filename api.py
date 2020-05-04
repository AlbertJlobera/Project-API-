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
    
    return f'<center><h1> Welcome {username}! :)</center> </h1><br><center><img src="https://optinmonster.com/wp-content/uploads/2017/09/perfect-welcome-email-for-new-subscribers.jpg"></center>'

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
            return f'<h1> Hello, {username} the new chat "{chatname}" is Created!</h1><br><center><img src="https://www.lavanguardia.com/r/GODO/LV/p5/WebSite/2018/04/12/Recortada/img_mrubal_20180412-112252_imagenes_lv_otras_fuentes_istock-819245942-kQsG-U442485828453q0E-992x558@LaVanguardia-Web.jpg"></center>''
        else:
            return f'<h1>Error: you are already in the chat.</h1><br><center><img src="https://www.lavanguardia.com/r/GODO/LV/p5/WebSite/2018/04/12/Recortada/img_mrubal_20180412-112252_imagenes_lv_otras_fuentes_istock-819245942-kQsG-U442485828453q0E-992x558@LaVanguardia-Web.jpg"></center>'


#Add message to a chat
@app.route('/chat/<chatname>/user/<username>/message/<message>')
@errorHandler
def findChatName(chatname, username, message):
    if db.unique.count_documents({'Name': username,'Chats': [chatname]}) == 0:
        raise Error404 (f'<h1> This user is not registered.</h1>')
    else:
        db.unique.update({'Name': username},{'$set':{"Messages": [message]}})
        return f'<h1><center> Thank you for your message! </center></h1><br><center><img src="https://image.shutterstock.com/image-vector/new-chat-messages-notification-on-260nw-1040460781.jpg"></center>'


# Get all message from chat name
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
        
@app.route('/')
def infoAPI():
    return f'<center><h1><strong> Welcome to my professional API </strong></h1> <p>My name is Albert and I will explain very quickly the basic commands: <i> <br><p align=center>1. Create a new user to access th chats<br> 2.Join the chat you want to <br>3.Send message and try to be nice because we will know it!<p align=center ></i> <br><h3>For more info about it read my file Readme.md in my Github accound:<br> <strong>[https://github.com/AlbertJlobera/Project-API-]<h3></strong></p></center><br><center><img src=" https://www.kindpng.com/picc/m/226-2265116_team-working-png-png-download-fun-at-work.png"></center> '

app.run("0.0.0.0", PORT, debug=True)


 