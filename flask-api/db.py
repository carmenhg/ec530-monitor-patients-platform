from flask import Flask
from flask_pymongo import pymongo
CONNECTION_STRING = "mongodb+srv://carmenhg:PatalargaHG0207@cluster0.qol4e.mongodb.net/device?retryWrites=true&w=majority"
client = pymongo.MongoClient(CONNECTION_STRING)
# db = client.get_database('flask_mongodb_atlas')
# user_collection = pymongo.collection.Collection(db, 'user_collection')