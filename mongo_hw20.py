import os
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()
MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")

uri = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@eshkere.j1pkyzz.mongodb.net/?appName=eshkere"

client = MongoClient(uri, server_api=ServerApi('1'))

db_books = client.shop
collection_books = db_books.books

book = {'title': 'Гра престолів', "price": 1050,'year': 1996, 'pages': 800}
collection_books.insert_one(book)

school_books = [
    {'title': 'Маленький принц', "class": 7, 'pages': 96},
    {'title': 'Шинель', "class": 9, 'pages': 48},
    {'title': 'Портрет Доріана Грея', "class": 9, 'pages': 320},
    {'title': 'Останній листок', "class": 8, 'pages': 16},
    {'title': '451° за Фаренгейтом', "class": 9, 'pages': 256}
]
created_books = collection_books.insert_many(school_books)

query = {'year': 2022}
for book in collection_books.find(query).sort('class', -1).limit(3):
    print(book)

for book in collection_books.find().sort('pages', -1).limit(1):
    print(book)

query = {'class': {"$gte": 5, "$lte": 8}}

for book in collection_books.find(query):
    print(book)
