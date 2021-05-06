from flask import current_app as app


def create_task(cmd):
    doc =  app.mongo.db.task.insert({"cmd":cmd, "status":"pending"})
    print(doc)
    return str(doc)

def get_task(taskid):
    task = app.mongo.db.task.find_one({"_id":taskid})
    return task