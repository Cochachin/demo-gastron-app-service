import json
from flask import request, jsonify
from flask_restplus import Namespace, Resource, fields, reqparse
from ..models.dto.SchemaAuthDto import SchemaAuthDto
from ..datasource.User_dao import User_dao
from ..datasource.Person_dao import Person_dao
from ..datasource.AccessToken_dao import AccessToken_dao
from ..models.dto.LoginResponse import LoginResponse
from ..models.dto.RegisterResponse import RegisterResponse
from ..models.dto.PersonResponse import PersonResponse
from ..models.constant.Constant import Constant
from ..models.entity.general.ErrorAPI import ErrorAPI

auth = SchemaAuthDto.auth
user_auth = SchemaAuthDto.login
user_register = SchemaAuthDto.register
any_response = SchemaAuthDto.any_response
login_response = SchemaAuthDto.login_response
user_response = SchemaAuthDto.user_response

parser = reqparse.RequestParser()
parser.add_argument('Authorization', type=str, location='headers', help='Access token', required=True)
parser.add_argument('user_id', type=str, location='args')

@auth.route('/login')
class AuthController(Resource):
    @auth.doc('user authentification')
    @auth.response(200, 'ok')
    @auth.expect(user_auth, validate=True)
    @auth.marshal_with(login_response)
    def post(self):
        response = LoginResponse(Constant.state_ok, Constant.ok)
        try:      
            request_data = request.json
            user_dao = User_dao()
            temp = user_dao.getUserByEmail(request_data["email"])
            if(temp is None):
                response.state = Constant.state_business
                response.message = Constant.error_bisiness
                response.addError(ErrorAPI(Constant.state_business, "Lo sentimos esta cuenta no esta registrado"))
            else:
                if temp.checkPassword(request_data["password"]):    
                    acess_dao = AccessToken_dao()
                    token = acess_dao.createSession(temp.id)
                    response.state = Constant.state_ok
                    response.message = Constant.ok
                    response.data = token
                else:
                    response.state = Constant.state_business
                    response.message = Constant.error_bisiness
                    response.addError(ErrorAPI(Constant.state_business, "Email o password incorrectos"))
        except:
            response.state = Constant.state_aplication
            response.message = Constant.error_application
        
        return response
    
@auth.route('/register')    
class AuthRegisterController(Resource):
    @auth.doc("user register")
    @auth.response(200, 'ok')
    @auth.expect(user_register, validate=True)
    @auth.marshal_with(any_response)
    def post(self):
        response = RegisterResponse(Constant.state_ok, Constant.ok)
        try:
            request_data = request.json
            user_dao = User_dao()
            temp = user_dao.getUserByEmail(request_data["email"])
            if(temp is None):
                user_dao.registerNewUser(request_data)
            else:
                response.state = Constant.state_business
                response.message = Constant.error_bisiness
                response.addError(ErrorAPI(Constant.state_business, "Lo sentimos usted tiene una cuenta creada"))
        except:
            response.state = Constant.state_aplication
            response.message = Constant.error_application
        
        return response

@auth.route('/users')    
class AuthRegisterController(Resource):
    @auth.doc(parser=parser)
    @auth.response(200, 'ok')
    @auth.marshal_with(user_response)
    def get(self):
        response = PersonResponse(Constant.state_ok, Constant.ok)
        try:
            user_id = request.args.get('user_id')
            person_dao = Person_dao()
            person = person_dao.getPerson(user_id)
            response.setPerson(person)
        except:
            response.state = Constant.state_aplication
            response.message = Constant.error_application
            
        return response
            