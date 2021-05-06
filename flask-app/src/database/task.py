from flask import current_app as app
from bson.objectid import ObjectId
import asyncio
from src.task.run_task import actual_task
from threading import Thread


def create_task(cmd):
    doc = app.mongo.db.task.insert({"cmd": cmd, "status": "not_started"})
    print("starting thread")
    Thread(target=actual_task, args=(doc,app.mongo.db)).start()
    return doc


def get_task(taskid):
    task = app.mongo.db.task.find_one({"_id": ObjectId(taskid)})
    return task
