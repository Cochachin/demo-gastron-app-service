class Base:
    def __init__(self, state, message):
        self.state = state
        self.message = message
        self.errorList = []
    
    def addError(self, error):
        self.errorList.append(error)
        