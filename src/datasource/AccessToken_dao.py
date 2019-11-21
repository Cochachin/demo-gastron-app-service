import uuid
import datetime
from ..models.entity.AccessToken import AccessToken
from ..config.Mongodb import Mongodb

class AccessToken_dao:
    def __init__(self):
        self.mongodb = Mongodb.getInstance()
    
    def createSession(self, user_id):
        accessToken_db = self.mongodb.db.access_token
        temp = accessToken_db.find_one({"user_id": user_id})
        if temp is None:
            accessToken_db.insert_one(
                    {"_id": uuid.uuid1(), 
                     "created_at": datetime.datetime.now(), 
                     "user_id": user_id,
                     "token": uuid.uuid1()})
        else:
            accessToken_db.update(
                { "user_id": user_id },
                {
                    "_id":temp["_id"],
                    "created_at": datetime.datetime.now(),
                    "user_id":temp["user_id"],
                    "token": uuid.uuid1()
                }
            )
            
        temp = accessToken_db.find_one({"user_id": user_id})
        return AccessToken(temp)        
        
        