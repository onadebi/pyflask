import os;

class Config(object):
    SECRETE_KEY = os.environ.get('supersecrete_key') or 'you-will-never-guess_theKey🙂';
