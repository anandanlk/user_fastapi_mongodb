from pymongo import MongoClient
import ssl
import certifi
ca = certifi.where()
uri = "mongodb+srv://anandanlk:5RNyJDr4PAnVZXh3@cluster0.c8inxge.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client['communityFL']['users']