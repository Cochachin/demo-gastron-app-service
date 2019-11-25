from flask import Flask, Blueprint
from flask_restplus import Api
from flask_cors import CORS

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, doc='/docs')

from src.controller.AuthController import auth as auth
from src.controller.RestaurantController import restaurant as restaurant

api.add_namespace(auth)
api.add_namespace(restaurant)

app = Flask(__name__)
app.register_blueprint(blueprint)
CORS(app)

if __name__ == '__main__':
    app.run()
