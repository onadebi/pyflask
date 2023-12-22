from flask import Flask;
from config import Config;
from flask_pymongo import PyMongo
import sys;


app = Flask(__name__)
app.config.from_object(Config);

print(f'DB cvalue from APP CONFIG:: {app.config["MONGO_URI"]}')
mongoCon: PyMongo;


try:
    mongoCon = PyMongo(app);
    # mongoCon.db = 
    print(mongoCon.db.list_collection_names())
    print('****MongoDB Connected!****')
except Exception as ex:
    print(f"****DB Connection ERROR: {ex}****")
    # Exit the application if the database connection fails
    sys.exit("Exiting application due to database connection failure")

from application import routes;

