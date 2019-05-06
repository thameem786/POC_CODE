import pymongo
from pymongo import MongoClient
mongo_instance_url = 'mongodb://mongoadmin:mongoadmin@<ip address>:27017/'
client = MongoClient(mongo_instance_url)
db = client['<db name>']
collection = db["ClassifiedGenericKnowledge.files"]
db_details = collection.find({},{"FileName":1,"Title":1,"_id":0})
for i in db_details:
    print(i)
