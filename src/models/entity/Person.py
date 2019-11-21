class Person:
    def __init__(self, data):
        self.fullName = data["fullnames"]
        self.sureName = data["surnames"]
        self.phone = data["phone"]
        self.user_id = data["user_id"]
    