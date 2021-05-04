from flask import Blueprint, request, jsonify
from database import task
api = Blueprint("api", __name__)


@api.route("/new_task", methods=['POST'])
def new_task():
    cmd = request.form['cmd']
    id = task.create_task(cmd)
    return jsonify({
        "id":id
    })

@api.route("/get_output/<id>", methods=["GET"])
def get_output(id):
    doc = task.get_task(id)
    if doc is None:
        return jsonify({
            "error":"Invalid task id"
        })
    return jsonify({
        "_id":str(doc['_id']),
        "cmd":doc['cmd'],
        "status":"pending"
    })