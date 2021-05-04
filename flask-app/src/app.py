from flask import Flask
from routes.routes import api
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/datagran"

app.mongo = PyMongo(app)

app.register_blueprint(api)

@app.route('/')
def hello():
    return 'This Compose/Flask demo has been viewed %s time(s).'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True) 