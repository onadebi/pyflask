from application import mongoCon;
from application.models import User;

class UserService():
    def __init__(self) -> None:
        self.db = mongoCon.db;
    
    def create_user(self, user_data: {}) -> bool:
        try:
            # user_data.first_name = user_data.first_name.capitalize();
            for key,val in user_data.items() :
                print(f"****User Data: [{key}]:[{val}] {user_data}****");
            self.db.users.insert_one(user_data);
            return True;
        except Exception as ex:
            print(f"****DB Connection ERROR: {ex}****")
            return False;
    