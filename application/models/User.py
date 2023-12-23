

class User:
    def __init__(self,user_id: int, first_name:str, last_name: str, email: str, password: str, **kwargs) -> None:
        self.user_id = user_id;
        self.first_name = first_name;
        self.last_name = last_name;
        self.email = email;
        self.password = password;
        self.__dict__.update(kwargs);

