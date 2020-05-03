from flask import Flask, request, jsonify
import pymongo
from bson.json_util import dumps
from config import PORT
from mongo import *
from errorHandler import *
import nltk
from api import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download("vader_lexicon")

# Calculating sentiment with `NLTK` sentiment analysis
@app.route('/chat/<chatname>/sentiment')
@errorHandler
def getAnalysts(chatname):
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
    for sentence in flat_list:
        sentiment = sia.polarity_scores(sentence)
    return dumps(sentiment)