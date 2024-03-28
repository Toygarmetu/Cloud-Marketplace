# from pymongo import MongoClient
# def get_db_handle(db_name, host, port, username, password):

#  client = MongoClient(host=host,
#                       port=int(port),
#                       username=username,
#                       password=password
#                      )
#  db_handle = client['cengden_db']
#  return db_handle, client



from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://atestoygar:leamk123@cengden.gcx1t1k.mongodb.net/?retryWrites=true&w=majority&appName=CENGDEN"

# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

def get_mongo_client():
    client = MongoClient(uri, server_api=ServerApi('1'))
    return client

# Function to ping the database
def ping_db(client):
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)