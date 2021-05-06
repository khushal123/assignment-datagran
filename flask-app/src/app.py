from flask import Flask
from src.routes.routes import api
from flask_pymongo import PyMongo



app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://mongo:27017/datagran"
app.mongo = PyMongo(app)
app.register_blueprint(api)


@app.route('/')
def hello():
    return 'This Compose/Flask demo has been viewed %s time(s).'


if __name__ == "__main__":
    app.run()
