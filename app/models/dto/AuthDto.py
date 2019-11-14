from flask_restplus import Namespace, fields

class AuthDto:
    auth = Namespace('auth', description='user authentification')
    login = auth.model('login', {
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password'),
    })
    
    register = auth.model('register', {
        'fullname':fields.String(required=True, description='user name'),
        'surname':fields.String(required=True, description='user surname'),
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password'),
    })