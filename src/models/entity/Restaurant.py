from ..constant.Constant import Constant

class Restaurant:
    def __init__(self, data):
        self.id = data["_id"]
        self.name = data["name"]
        self.address = data["address"]
        self.region = data["region"]
        self.district = data["district"]
        self.ranking = data["ranking"]
        self.open_close = data["open_close"]
        self.comment_negative = data["comment_negative"]
        self.comment_positive = data["comment_positive"]
    
    def generateRanking(self, data, flag):
        if flag == Constant.COMMENT_POSITIVE:
            data.comment_positive = data.comment_positive + 1
        elif flag == Constant.COMMENT_NEGATIVE:
            data.comment_negative = data.comment_negative + 1
            
        total = data.comment_positive - data.comment_negative
        data.ranking = self.getRanking(total)
        
        return data
    
    def getRanking(self, total):
        if total <= 0:
            return 0
        elif total <= Constant.RANKING_1:
            return 1
        elif total <= Constant.RANKING_2:
            return 2
        elif total <= Constant.RANKING_3:
            return 3
        elif total <= Constant.RANKING_4:
            return 4
        else:
            return 5
            
            