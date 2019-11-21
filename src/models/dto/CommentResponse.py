from .Base import Base
class CommentResponse(Base):
    
    def __init__(self, state, message):
        super().__init__(state, message)
    
    def setComment(self, data):
        self.data = data