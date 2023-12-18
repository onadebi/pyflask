from flask import Flask;
from config import Config;
from flask_pymongo import PyMongo;


app = Flask(__name__)
app.config.from_object(Config);
# app.config['MONGO_URI'] = 'mongodb://localhost:27017/mydatabase'
print(f'DB cvalue from APP CONFIG:: {app.config["MONGO_URI"]}')
mongoCon: PyMongo;

try:
    mongoCon = PyMongo(app);
    print('****MongoDB Connected!****')
except Exception as ex:
    print(f"****DB Connection ERROR: {ex}****")

from application import routes;

