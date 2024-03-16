from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app, origins=["http://localhost:8081"])
app.config['MONGODB_SETTINGS'] = {
    'db': 'songomondageDB',
    'host': 'mongodb://localhost:27017/',
}

client = MongoClient('mongodb://localhost:27017/')
db = client['songomondageDB']