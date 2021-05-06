from flask import current_app as app
from bson.objectid import ObjectId
import asyncio
from src.task.run_task import actual_task


def create_task(cmd):
    doc = app.mongo.db.task.insert({"cmd": cmd, "status": "not_started"})
    return doc


def get_task(taskid):
    print("this is taskid=>%s", taskid)
    task = app.mongo.db.task.find_one({"_id": ObjectId(taskid)})
    print(task.get("cmd"))
    return task
