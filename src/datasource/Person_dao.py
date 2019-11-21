from ..config.Mongodb import Mongodb
from ..models.entity.Person import Person
import uuid

class Person_dao:
    def __init__(self):
        self.mongodb = Mongodb.getInstance()
    
    def getPerson(self, user_id):
        person_db = self.mongodb.db.person
        temp = person_db.find_one({"user_id":uuid.UUID(user_id)})
        if(temp is None):
            return None
        else:    
            return Person(temp)
        