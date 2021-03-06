import asyncio
import subprocess
import time

db = None

def update_task(id, data):
    update = db.task.update_one({
        "_id": id
    }, {
        "$set": data
    })

async def execute_command(cmd, id):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    print(f'[{cmd!r} exited with {proc.returncode}]')
    output = ""
    if stdout:
        output = stdout.decode("utf-8")
        print(f'[stdout]\n{output}')
    if stderr:
        output = stderr.decode("utf-8")
        print(f'[stderr]\n{output}')
    update_task(id, {
        "status": 'finished',
        "output": output
    })


# def actual_task():
#     tasks = db.task.find({
#         "status": "not_started"
#     })
#     for task in tasks:
#         # update_ids.append(task.get("_id"))
#         id = task.get("_id")
#         update_task(id, {
#             "status": "running"
#         })
#         cmd = task.get("cmd")
#         asyncio.run(execute_command(cmd, id))


def actual_task(taskid, db):
    globals()['db'] = db
    print(db)
    task = db.task.find_one({
        "_id": taskid
    })
    id = task.get("_id")
    print("updating status")
    update_task(id, {
        "status": "running"
    })
    
    cmd = task.get("cmd")
    print("running command")
    asyncio.run(execute_command(cmd, id))
    time.sleep(1)
    

# update_tasks = db.task.update_many({
#     "_id": {"$in": update_ids}
# }, {
#     "$set": {
#         "status": "running"
#     }
# })
