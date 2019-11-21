from .Base import Base

class RegisterResponse(Base):
    def __init__(self, state, message):
        super().__init__(state, message)
    
        