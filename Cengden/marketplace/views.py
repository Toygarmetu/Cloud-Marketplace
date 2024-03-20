import datetime
import time
from pymongo import MongoClient
import os
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

client = MongoClient('mongodb+srv://atestoygar:leamk123@cengden.gcx1t1k.mongodb.net/')

dbname = client['cengden_db']

collection = dbname['phone']

phone_1 = {
    "brand": "Samsung",
    "model": "Galaxy S21",
    "price": 800,
}

collection.insert_one(phone_1)

