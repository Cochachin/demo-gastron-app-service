from flask_restplus import Namespace, fields

class SchemaAuthDto:
    auth = Namespace('auth', description='schema machine learning')
    
    login = auth.model('login', {
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password')
    })
    
    register = auth.model('register', {
        'fullnames':fields.String(required=True, description='user name'),
        'surnames':fields.String(required=True, description='user surname'),
        'phone': fields.String(required=True, description='user surname'),
        'email': fields.String(required=True, description='user email address'),
        'password': fields.String(required=True, description='user password')
    })
    
    error = auth.model('error', {
        'code':fields.Integer(required=True, description='user name'),
        'message':fields.String(required=True, description='user surname')
    }) 
    
    any_response = auth.model('any_response', {
        'state':fields.Integer(required=True, description='user name'),
        'message':fields.String(required=True, description='user surname'),
        'errorList':fields.List(fields.Nested(error))
    })
    
    access_token = auth.model('access_token', {
        'id':fields.String(),
        'created_at':fields.Date(),
        'user_id': fields.String(),
        'token': fields.String()
    })
    
    login_response = auth.model('login_response', {
        'state':fields.Integer(required=True, description='user name'),
        'message':fields.String(required=True, description='user surname'),
        'data': fields.Nested(access_token),
        'errorList':fields.List(fields.Nested(error))
    })
    
    person = auth.model('person', {
        'fullName':fields.String(required=True, description='user fullname'),
        'sureName':fields.String(required=True, description='user surnames'),
        'phone':fields.String(required=True, description='user phone'),
        'email': fields.String(required=True, description='user phone'),
        'user_id':fields.String(required=True, description='user id')
    })
    
    user_response = auth.model('user_response', {
        'state':fields.Integer(required=True, description='user name'),
        'message':fields.String(required=True, description='user surname'),
        'data': fields.Nested(person),
        'errorList':fields.List(fields.Nested(error))
    })
    