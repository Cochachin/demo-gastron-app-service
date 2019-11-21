class AccessToken:
    def __init__(self, data):
        self.id = data["_id"]
        self.created_at = data["created_at"]
        self.user_id = data["user_id"]
        self.token = data["token"]
        