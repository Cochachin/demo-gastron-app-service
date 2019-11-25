import json
from flask import request, jsonify
from flask_restplus import Namespace, Resource, fields, reqparse
from ..models.dto.SchemaRestaurantDto import SchemaRestaurantDto
from ..datasource.Restaurant_dao import Restaurant_dao
from ..datasource.Comment_dao import Comment_dao
from ..models.dto.RestaurantResponse import RestaurantResponse
from ..models.dto.CommentResponse import CommentResponse
from ..models.constant.Constant import Constant
from ..ml.SVM import SVM

restaurant = SchemaRestaurantDto.restaurant
restaurant_response = SchemaRestaurantDto.restaurant_response
comment_response = SchemaRestaurantDto.comment_response
comment_list_response = SchemaRestaurantDto.comment_list_response
comment = SchemaRestaurantDto.comment

parser = reqparse.RequestParser()
parser.add_argument('Authorization', type=str, location='headers', help='Access token', required=True)
parser_1 = reqparse.RequestParser()
parser_1.add_argument('Authorization', type=str, location='headers', help='Access token', required=True)
parser_1.add_argument('search', type=str, location='args')

parser_2 = reqparse.RequestParser()
parser_2.add_argument('restaurant_id', type=str, location='args')
 

@restaurant.route('/')
class RestaurantController(Resource):
    @restaurant.doc(parser=parser_1)
    @restaurant.response(200, 'ok')
    #@restaurant.marshal_with()
    @restaurant.marshal_with(restaurant_response)
    def get(self):
        response = RestaurantResponse(Constant.state_ok, Constant.ok)
        search = request.args.get('search')
        restaurant_dao = Restaurant_dao()
        tempList = restaurant_dao.searchRestaurant(search)
        response.setRestaurantList(tempList)
        return response;

@restaurant.route('/comments')
@restaurant.doc(parser=parser)
class RestaurantCommenstController(Resource):
    @restaurant.expect(comment, validate=True)
    @restaurant.response(200, 'ok')
    @restaurant.marshal_with(comment_response)
    def post(self):
        svm = SVM()
        comment_data = request.json
        response = CommentResponse(Constant.state_ok, Constant.ok)
        comment_dao = Comment_dao()
        flag = svm.rateComment(comment_data["message"])
        restaurant_dao = Restaurant_dao()
        rest_data = restaurant_dao.getRestaurant(comment_data["restaurant_id"])
        rest_data = rest_data.generateRanking(rest_data, flag)
        restaurant_dao.updateRestaurant(rest_data)
        temp = comment_dao.createComment(comment_data, flag)
        response.setComment(temp)
        return response
    
    @restaurant.doc(parser=parser_2, required=True)
    @restaurant.response(200, 'ok')
    @restaurant.marshal_with(comment_list_response)
    def get(self):
        response = CommentResponse(Constant.state_ok, Constant.ok)
        restaurant_id = request.args.get('restaurant_id')
        comment_dao = Comment_dao()
        temp = comment_dao.getComements(restaurant_id)
        response.setComment(temp)
        return response

@restaurant.route('/comments/replies')
@restaurant.doc(parser=parser)
class RestaurantCommenstController(Resource):
    @restaurant.expect(comment, validate=True)
    @restaurant.response(200, 'ok')
    @restaurant.marshal_with(comment_response)
    def post(self):
        try:
            comment_data = request.json
            response = CommentResponse(Constant.state_ok, Constant.ok)
            comment_dao = Comment_dao()
            temp = comment_dao.createComment(comment_data)
            response.setComment(temp)
        except:
            response.state = Constant.state_aplication
            response.message = Constant.error_application
                
        return response
            