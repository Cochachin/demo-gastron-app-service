from .Person import Person

class Comment_replay:
    def __init__(self, data):
        self.message = data["message"]
        self.comment_id = data["comment_id"]
        self.user = Person(data["user"])
    