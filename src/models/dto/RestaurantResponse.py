from .Base import Base

class RestaurantResponse(Base):
    def __init__(self, state, message):
        super().__init__(state, message)
        
    def setRestaurantList(self, data):
        self.data = data
        