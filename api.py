from flask import Flask, request
import pymongo
from bson.json_util import dumps


app=Flask(__name__)

#Create User
@app.route("/user/create/<username>")
def new_user(username):
    data = { "name": f"{username}"}
    user = users.insert_one(data)
    return dumps(user.inserted_id)

app.run("0.0.0.0", 3500, debug=True)


