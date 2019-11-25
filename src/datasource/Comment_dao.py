import datetime
from ..config.Mongodb import Mongodb
import uuid
from ..models.entity.Comment import Comment

class Comment_dao:
    def __init__(self):
        self.mongodb = Mongodb.getInstance()
    
    def getCommentList(self, restaurant_id):
        comment_db = self.mongodb.db.comment
        #tempList = restaurant_db.find({})
    
    def createRepliesComment(self, request):
        comment = Comment(None)
        comment_db = self.mongodb.db.comment
        person_db = self.mongodb.db.person
        person = person_db.find_one({"user_id":uuid.UUID(request["user_id"])})
        id = uuid.uuid1()
        temp = {
                    "_id": id,
                    "created_at":datetime.datetime.now(),
                    "message": request["message"], 
                    "restaurant_id": request["restaurant_id"],
                    "type": "replies",
                    "user": {
                        "fullnames": person["fullnames"],
                        "surnames": person["surnames"],
                        "phone": person["phone"],
                        "user_id": uuid.UUID(request["user_id"])
                    },
                    "comment_replay": []
                }
        comment_db.insert_one(temp)
        return Comment(temp)
    
    def createComment(self, request, flag):
        comment = Comment(None)
        typeComment = comment.getTypeCommment(flag)
        comment_db = self.mongodb.db.comment
        person_db = self.mongodb.db.person
        person = person_db.find_one({"user_id":uuid.UUID(request["user_id"])})
        print(person)
        id = uuid.uuid1()
        temp = {
                    "_id": id,
                    "created_at":datetime.datetime.now(),
                    "message": request["message"], 
                    "restaurant_id": request["restaurant_id"],
                    "type": typeComment,
                    "user": {
                        "fullnames": person["fullnames"],
                        "surnames": person["surnames"],
                        "phone": person["phone"],
                        "user_id": uuid.UUID(request["user_id"])
                    },
                    "comment_replay": []
                }
        comment_db.insert_one(temp)
        return Comment(temp)

    def getComements(self, restaurant_id):
        response = []
        comment_db = self.mongodb.db.comment
        tempList = comment_db.find({"restaurant_id": restaurant_id})
        for item in tempList:
            temp = Comment(item)
            for it in item["comment_replay"]:
                temp.comment_replay.append(Comment(it))
                
            response.append(temp)
            
        return response
            
        