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
        print(bcrypt.checkpw(code, hashed), "hello")
        if bcrypt.checkpw(code, hashed) is True:
            return True
        else:
            return False