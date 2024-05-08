from pymongo import MongoClient
mongodb_uri = 'mongodb+srv://anandanlk:5RNyJDr4PAnVZXh3@cluster0.c8inxge.mongodb.net/'
port = 8000
client = MongoClient(mongodb_uri, port)
db = client["User"]