import datetime
import time
from pymongo import MongoClient
import os
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello Cengden project!</h1>")


client = MongoClient('mongodb+srv://atestoygar:leamk123@cengden.gcx1t1k.mongodb.net/')

dbname = client['cengden_db']

collection = dbname['phone']

phone_1 = {
    "brand": "Samsung",
    "model": "Galaxy S21",
    "price": 800,
}

collection.insert_one(phone_1)

