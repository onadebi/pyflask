import os;

class Config(object):
    SECRETE_KEY = os.environ.get('supersecrete_key') or 'you-will-never-guess_theKey🙂';

    # Database configuration
    # MONGO_CONNECT = False;
    PDB = os.environ.get('DB_CON');
    print(f'rtyuioiuytr:::{PDB}')
    MONGO_URI = os.environ.get('DB_CON');
