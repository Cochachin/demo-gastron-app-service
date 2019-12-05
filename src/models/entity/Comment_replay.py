from .Person import Person

class Comment_replay:
    def __init__(self, data):
        self.id=data["_id"]
        self.message = data["message"]
        self.comment_id = data["comment_id"]
        self.user = Person(data["user"])
    