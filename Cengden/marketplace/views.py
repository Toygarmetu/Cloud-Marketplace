import datetime
import time
from pymongo import MongoClient
import os
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def categories(request):
    return render(request, 'categories.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')

def category_items(request):
    return render(request, 'category_items.html')

client = MongoClient('mongodb+srv://atestoygar:leamk123@cengden.gcx1t1k.mongodb.net/')

dbname = client['cengden_db']

collection = dbname['phone']

phone_1 = {
    "brand": "Samsung",
    "model": "Galaxy S21",
    "price": 800,
}

collection.insert_one(phone_1)

