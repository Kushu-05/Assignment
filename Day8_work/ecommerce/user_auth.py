class UserAuth:
    def __init__(self):
        self.users ={"admin" : "admin123"}
    def register(self,username,password):
        if username in self.users:
            return False 
        self.users[username]=password
        return True
    def login(self,username,password):
        return self.users.get(username)==password