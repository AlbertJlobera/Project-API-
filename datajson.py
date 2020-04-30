import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["API_Project"]
mycol = mydb["API"]

users = { 'Albert': 'Holi caracoli'
}

x = mycol.insert_one(mydict)
