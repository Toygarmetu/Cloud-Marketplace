import datetime
import time
from pymongo import MongoClient
import os
from django.http import HttpResponse
from django.shortcuts import render
from .utils import get_mongo_client
from bson.json_util import dumps
from bson.objectid import ObjectId
from bson.errors import InvalidId
from django.core.paginator import Paginator
from pymongo import MongoClient, DESCENDING



from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from marketplace.models import Item
from marketplace.serializers import ItemSerializer


@csrf_exempt
def itemApi(request, id=0):
    if request.method == 'GET':
        items = Item.objects.all()
        items_serializer = ItemSerializer(items, many=True)
        return JsonResponse(items_serializer.data, safe=False)
    elif request.method == 'POST':
        item_data = JSONParser().parse(request)
        item_serializer = ItemSerializer(data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to add", safe=False) 
    elif request.method == 'PUT':
        item_data = JSONParser().parse(request)
        item = Item.objects.get(id=item_data['id'])
        item_serializer = ItemSerializer(item, data=item_data)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("Updated successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method == 'DELETE':
        item = Item.objects.get(id=id)
        item.delete()
        return JsonResponse("Deleted successfully", safe=False)


def index(request):
    # Use your MongoDB Atlas URI directly here
    client = MongoClient("mongodb+srv://atestoygar:leamk123@cengden.gcx1t1k.mongodb.net/?retryWrites=true&w=majority&appName=CENGDEN")
    db = client['cengden_db']
    
    
    items_list = []
    for category_name in ['computers', 'phones', 'private_lessons', 'vehicle']:
        category_collection = db[category_name]
        # Fetch items from each category
        category_items = list(category_collection.find().limit(25))  # Adjust the limit as needed
        items_list.extend(category_items)
    
    # Convert ObjectId to datetime for sorting, using the ObjectId generation time as a fallback
    for item in items_list:
        if 'created_at' not in item:
            # Use the ObjectId's generation time as a fallback
            item['created_at'] = item['_id'].generation_time

    # Now sort the combined list by 'created_at'
    items_list.sort(key=lambda x: x['created_at'], reverse=True)

    # Truncate the list to only include the latest 100 items
    items_list = items_list[:100]

    # Set up pagination
    paginator = Paginator(items_list, 10)  # Show 10 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    client.close()
    return render(request, 'index.html', {'page_obj': page_obj})

def item_detail(request, id):
    client = get_mongo_client()
    db = client['cengden_db']
    
    # Assuming 'computers' collection, change accordingly if it's a different collection
    item = db['computers'].find_one({'_id': ObjectId(id)})

    client.close()
    
    if item is not None:
        # Convert the _id field to a string to avoid serialization issues in the template
        item['_id'] = str(item['_id'])
        context = {'item': item}
        return render(request, 'item_detail.html', context)
    else:
        # If no item is found, you might want to redirect to a 404 page or display an error message
        pass



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

