import datetime
from ..config.Mongodb import Mongodb
import uuid
from ..models.entity.Comment_replay import Comment_replay
from ..models.entity.Person import Person
from ..models.entity.Comment_replay import Comment_replay

class Comment_replay_dao:
    def __init__(self):
        self.mongodb = Mongodb.getInstance()
        
    def createRepliesComment(self, request):
            comment_replay_db = self.mongodb.db.comment_replay
            person_db = self.mongodb.db.person
            person = person_db.find_one({"user_id":uuid.UUID(request["user_id"])})
            id = uuid.uuid1()
            temp = {
                        "_id": id,
                        "created_at":datetime.datetime.now(),
                        "message": request["message"], 
                        "comment_id": uuid.UUID(request["comment_id"]),
                        "type": "replies",
                        "user": {
                            "fullnames": person["fullnames"],
                            "surnames": person["surnames"],
                            "email": person["email"],
                            "phone": person["phone"],
                            "user_id": uuid.UUID(request["user_id"])
                        }
                    }
            comment_replay_db.insert_one(temp)
            return Comment_replay(temp)