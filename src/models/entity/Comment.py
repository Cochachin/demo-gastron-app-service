class Comment:
    def __init__(self, data):
        self.id = data["_id"]
        self.message = data["message"]
        self.created_at = data["created_at"]
        self.restaurant_id = data["restaurant_id"]
        self.user_id = data["user_id"]
        self.comment_replay = []
       
        