from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'songomondageDB',
    'host': 'mongodb://localhost:27017/',
}

client = MongoClient('mongodb://localhost:27017/')
db = client['songomondageDB']