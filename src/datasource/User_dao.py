import uuid
from ..config.Mongodb import Mongodb
from ..helpers.HelperPassword import HelperPassword
from ..models.entity.User import User

class User_dao:
    def __init__(self):
        self.mongodb = Mongodb.getInstance()
        self.client = self.mongodb.client
    
    def registerNewUser(self, request):
        person_db = self.mongodb.db.person
        user_db = self.mongodb.db.user
        id = uuid.uuid1()
        password = HelperPassword.bcryptPassword(request["password"]);
        data_1 = user_db.insert_one(
                    {"_id": id, 
                     "password": password, 
                     "email": request["email"]})
        data_2 = person_db.insert_one(
                    {"_id": uuid.uuid1(), "fullnames": request["fullnames"], 
                     "surnames": request["surnames"],
                     "user_id": id,
                     "phone": request["phone"]})
        
    def getUserByEmail(self, email):
        user_db = self.mongodb.db.user
        temp = user_db.find_one({"email": email})
        if(temp is None):
            return None
        else:
            return User(temp)
        
                
        
        