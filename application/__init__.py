from flask import Flask;
from config import Config;
from flask_pymongo import PyMongo;
import sys;


app = Flask(__name__)
app.config.from_object(Config);

print(f'DB value from APP CONFIG:: {app.config["MONGO_URI"]}')
mongoCon: PyMongo;


try:
    
    mongoCon = PyMongo(app);
    print(mongoCon.db.list_collection_names())

    #region ==============Database properties Initializers

    user_collection = mongoCon.db.get_collection('user')
    # Check if the index already exists
    existing_indexes = user_collection.index_information();
    for i in existing_indexes:
        print(f'{i} \n')
    if 'user_id_1' not in existing_indexes:
    # The create_index method is called with the argument ('user_id', 1) to create an index on the user_id field in ascending order (1).
    # The unique=True parameter is added to make the index unique.
        mongoCon.db.get_collection('user').create_index([('user_id', 1)], unique=True)
    if 'email_idx_unique' not in existing_indexes:
         mongoCon.db.get_collection('user').create_index([('email', 1)],name='email_idx_unique', unique=True)
    # Setting limits on field enties
    print('\n\n\t\t====Setting limits on field enties====\n\n')
    mongoCon.db.get_collection('user').database.command('collMod',"user", validator={
        "$jsonSchema": {
            "bsonType": "object", "properties": {
                "first_name": {
                    "bsonType": "string", "maxLength": 50
                    },
                "last_name": {
                    "bsonType": "string", "maxLength": 50
                    },
                "email": {
                    "bsonType": "string", "maxLength": 30
                    },
                "password": {
                    "bsonType": "string", "maxLength": 30
                    }
                }
            }
        })
        #mongoCon.db.get_collection('user').create_index([('first_name', 1)], name="first_name_1", key=[("first_name", 1)], max_length=50)

    #endregion ====================
    print('****MongoDB Connected!****')
except Exception as ex:
    print(f"****DB Connection ERROR: {ex}****")
    # Exit the application if the database connection fails
    sys.exit("Exiting application due to database connection failure")

from application import routes;
