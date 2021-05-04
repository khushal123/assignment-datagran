from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.datagran

tasks = db.task.find({
    "status":"pending"
})

for task in tasks:
    print(task.get("_id"))