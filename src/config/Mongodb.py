from pymongo import MongoClient
class Mongodb:
    _intance = None
    @staticmethod
    def getInstance():
        if Mongodb._intance == None:
            Mongodb()
        return Mongodb.__instance;
        
    def __init__(self):
        self.client = MongoClient("mongodb://gastomapp:florian1712@ds255768.mlab.com:55768/amautadb?retryWrites=false")
        self.db = self.client["amautadb"]
        Mongodb.__instance = self      
    
    