from application import mongoCon; 


class DatabaseConfig():
    def __init__ (self)-> None:
        print(f"===========Set database properties==========");
        mongoCon.db.get_collection('users').create_index('user_id')