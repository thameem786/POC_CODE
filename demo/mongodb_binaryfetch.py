# import pymongo
# from pymongo import MongoClient
# mongo_instance_url = 'mongodb://mongoadmin:mongoadmin@192.168.31.138:27017/'
# client = MongoClient(mongo_instance_url)
# db = client['12041_quasar_300000000000000000000002']
# collection = db["ClassifiedGenericKnowledge.files"]
# db_details = collection.find_one({})
# print(db_details)

# W01ZV0laX1FVQVNBUl9UQUdfU0xJREVfMV0KTkVXIEpPSU4gT05CT0FSREl3d3Fkd05HIERFQ0suQ0FSRElOQUwgSEVBTFRILgpU...

import pymongo
from pymongo import MongoClient
mongo_instance_url = 'mongodb://mongoadmin:mongoadmin@<ip address>:27017/'
client = MongoClient(mongo_instance_url)
db = client['<db_name>']
collection = db["xxx.chunks"]
db_details = collection.find({})
print(db_details)
for i in db_details:
    print(i)
with open("parse.txt" ,"w") as f:
        f.write(str(i))
