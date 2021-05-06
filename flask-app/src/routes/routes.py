from flask import Blueprint, request, jsonify
from src.database import task
api = Blueprint("api", __name__)


@api.route("/new_task", methods=['POST'])
def new_task():
    cmd = request.form['cmd']
    if cmd is None:
        return jsonify({
            error:"cmd is empty"
        })
    id = task.create_task(cmd)
    return jsonify({
        "id": str(id)
    })


@api.route("/get_output/<id>", methods=["GET"])
def get_output(id):
    doc = task.get_task(id)
    if doc is None:
        return jsonify({
            "error": "Invalid task id"
        })
    taskdict = {
        "_id": str(doc['_id']),
        "cmd": doc['cmd'],
        "status": doc['status']
    }
    if(doc['output'] is not None):
        taskdict.update({"output":doc['output']})
    return jsonify(taskdict)
