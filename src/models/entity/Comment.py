from ..constant.Constant import Constant
from .Person import Person

class Comment:
    def __init__(self, data):
        if data is not None:
            self.id = data["_id"]
            self.message = data["message"]
            self.type = data["type"]
            self.created_at = data["created_at"]
            self.restaurant_id = data["restaurant_id"]
            self.user = Person(data["user"])
            self.comment_replay = []
    
    def getTypeCommment(self, flag):
        if flag == Constant.COMMENT_NEGATIVE:
            return Constant.COMMENT_NEGATIVE_TEXT
        else:
            return Constant.COMMENT_POSITIVE_TEXT
    
    def setUser(self, data):
        self.user = data
        