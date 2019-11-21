from src.helpers.HelperPassword import HelperPassword

class User:
    def __init__(self, data):
        self.id = data["_id"]
        self.email = data["email"]
        self.password = data["password"]
    
    def checkPassword(self, password):
        return HelperPassword.bcryptCheckPw(password, self.password)
        