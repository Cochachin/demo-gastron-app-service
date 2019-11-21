from ..config.Mongodb import Mongodb
from ..models.entity.Restaurant import Restaurant
from bson.objectid import ObjectId

class Restaurant_dao:
    def __init__(self):
        self.mongodb = Mongodb.getInstance()
        self.client = self.mongodb.client
    
    def searchRestaurant(self, search):
        response = []
        restaurant_db = self.mongodb.db.restaurant
        if search is None:
            tempList = restaurant_db.find().sort([("ranking", -1)])
        else:
            tempList = restaurant_db.find({"name": {"$regex": search, "$options" : "i"}}).sort([("ranking", -1)])
            
        for item in tempList:
            response.append(Restaurant(item))
            
        return response
    
    def getRestaurant(self, restaurant_id):
        restaurant_db = self.mongodb.db.restaurant            
        temp = restaurant_db.find_one({"_id": ObjectId(restaurant_id)})
        return Restaurant(temp)
    
    def updateRestaurant(self, data):
        restaurant_db = self.mongodb.db.restaurant
        restaurant_db.update(
                { "_id": data.id },
                {
                    "name": data.name,
                    "address": data.address,
                    "region": data.region,
                    "district": data.district,
                    "ranking": data.ranking,
                    "open_close": data.open_close,
                    "comment_negative": data.comment_negative,
                    "comment_positive": data.comment_positive
                }
            )