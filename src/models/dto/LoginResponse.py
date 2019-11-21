from .Base import Base
from ..entity.AccessToken import AccessToken

class LoginResponse(Base):
    def __init__(self, state, message):
        super().__init__(state, message)
        
    def setAccessToken(self, data):
        self.data = data
        