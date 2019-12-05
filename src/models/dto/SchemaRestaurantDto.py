from flask_restplus import Namespace, fields

class SchemaRestaurantDto:
    restaurant = Namespace('restaurant', description='schema machine learning')
    
    error = restaurant.model('error', {
        'code':fields.Integer(required=True, description='user name'),
        'message':fields.String(required=True, description='user surname')
    }) 
     
    restaurant_mo = restaurant.model('restaurant_mo', {
        'id':fields.String(required=True, description='user surname'),
        'name':fields.String(required=True, description='user surname'),
        'address': fields.String(required=True, description='user surname'),
        'region': fields.String(required=True, description='user surname'),
        'comment_negative': fields.Integer(required=True, description='user surname'),
        'comment_positive': fields.Integer(required=True, description='user surname'),
        'district': fields.String(required=True, description='user surname'),
        'ranking': fields.Integer(required=True, description='user surname'),
        'open_close': fields.String(required=True, description='user surname')
    })
    
    restaurant_response = restaurant.model('restaurant_response', {
        'state':fields.Integer(required=True, description='user name'),
        'message':fields.String(required=True, description='user surname'),
        'data': fields.List(fields.Nested(restaurant_mo)),
        'errorList':fields.List(fields.Nested(error))
    })
    
    person = restaurant.model('person', {
        'fullName':fields.String(required=True, description='user fullname'),
        'sureName':fields.String(required=True, description='user surnames'),
        'phone':fields.String(required=True, description='user phone'),
        'email':fields.String(required=True, description='user email'),
        'user_id':fields.String(required=True, description='user id')
    })
    
    other_commment = restaurant.model('other_commment', {
        'id':fields.String(description='user name'),
        'message':fields.String(required=True, description='user name'),
        'type':fields.String(description='user name'),
        'restaurant_id':fields.String(required=True, description='restaurant comment'),
        'user': fields.Nested(person)
    })
    
    comment = restaurant.model('comment', {
        'id':fields.String(description='user name'),
        'message':fields.String(required=True, description='user name'),
        'type':fields.String(description='user name'),
        'restaurant_id':fields.String(required=True, description='restaurant comment'),
        'user_id':fields.String(required=True, description='user comment'),
        'user': fields.Nested(person),
        'comment_replay': fields.List(fields.Nested(other_commment))
    })
    
    replay = restaurant.model('replay', {
        'message': fields.String(required=True, description='user name'),
        'user_id': fields.String(required=True, description='user comment'),
        'comment_id': fields.String(required=True, description='user comment')
    })
    
    replay_data = restaurant.model('replay_data', {
        'message': fields.String(required=True, description='user name'),
        'comment_id': fields.String(required=True, description='user comment'),
        'user': fields.Nested(person)
    })
    
    comment_response = restaurant.model('comment_response', {
        'state':fields.Integer(required=True, description='user name'),
        'message':fields.String(required=True, description='user surname'),
        'data': fields.Nested(comment),
        'errorList':fields.List(fields.Nested(error))
    })
    
    replay_response = restaurant.model('replay', {
        'state':fields.Integer(required=True, description='user name'),
        'message':fields.String(required=True, description='user surname'),
        'data': fields.Nested(replay_data),
        'errorList':fields.List(fields.Nested(error))
        
    })
    
    comment_list_response = restaurant.model('comment_list_response', {
        'state':fields.Integer(required=True, description='user name'),
        'message':fields.String(required=True, description='user surname'),
        'data': fields.List(fields.Nested(comment)),
        'errorList':fields.List(fields.Nested(error))
    })
    