import datetime
from ..config.Mongodb import Mongodb
import uuid
from bson.objectid import ObjectId
from ..models.entity.Comment import Comment
from ..models.entity.Comment_replay import Comment_replay
class Comment_dao:
    def __init__(self):
        self.mongodb = Mongodb.getInstance()
    
    def getCommentList(self, restaurant_id):
        comment_db = self.mongodb.db.comment
        #tempList = restaurant_db.find({})
    
    def createComment(self, request, flag):
        comment = Comment(None)
        typeComment = comment.getTypeCommment(flag)
        comment_db = self.mongodb.db.comment
        person_db = self.mongodb.db.person
        person = person_db.find_one({"user_id":uuid.UUID(request["user_id"])})
        id = uuid.uuid1()
        temp = {
                    "_id": id,
                    "created_at":datetime.datetime.now(),
                    "message": request["message"], 
                    "restaurant_id": ObjectId(request["restaurant_id"]),
                    "type": typeComment,
                    "user": {
                        "fullnames": person["fullnames"],
                        "surnames": person["surnames"],
                        "email": person["email"],
                        "phone": person["phone"],
                        "user_id": uuid.UUID(request["user_id"])
                    }
                }
        comment_db.insert_one(temp)
        return Comment(temp)

    def getComements(self, restaurant_id):
        response = []
        comment_db = self.mongodb.db.comment
        comment_replay_db = self.mongodb.db.comment_replay
        
        tempList = comment_db.find({"restaurant_id": ObjectId(restaurant_id)})
        for item in tempList:
            temp = Comment(item)
            list_1 =  comment_replay_db.find({"comment_id": temp.id})
            replay_list = []
            for item_1 in list_1:
                replay = Comment_replay(item_1)
                replay_list.append(replay)
                  
            temp.comment_replay = replay_list
            
            response.append(temp)

        return response
            
        