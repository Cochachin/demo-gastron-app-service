import bcrypt
import hashlib


class HelperPassword:
    
    @staticmethod
    def bcryptPassword(password):
        password = password.encode()
        salt = bcrypt.gensalt(rounds=16)
        hashed = bcrypt.hashpw(password, salt)
        return hashed
    
    @staticmethod
    def bcryptCheckPw(password, hashed):
        code = password.encode()
        if bcrypt.hashpw(code, hashed):
            return True
        else:
            return False