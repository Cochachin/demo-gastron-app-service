from flask_restplus import Namespace, Resource, fields
from ..models.dto.AuthDto import AuthDto

auth = AuthDto.auth
user_auth = AuthDto.login
user_register = AuthDto.register

#hello = Namespace('hello', description='Hello wordls')

@auth.route('/login')
class AuthController(Resource):
    @auth.doc('user authentification')
    @auth.response(200, 'ok')
    @auth.expect(user_auth, validate=True)
    def post(self):
        return {'id': 'hello', 'name': 'wordl'}
    
@auth.route('/register')    
class AuthRegisterController(Resource):
    @auth.doc("user register")
    @auth.response(200, 'ok')
    @auth.expect(user_register, validate=True)
    def post(self):
        return {'id': 'hello', 'name': 'wordl'}