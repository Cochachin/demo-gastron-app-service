from .Base import Base
class PersonResponse(Base):
    def __init__(self, state, message):
        super().__init__(state, message)
    
    def setPerson(self, data):
        self.data = data
        