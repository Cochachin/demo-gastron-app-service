from flask import Flask, Blueprint
from flask_restplus import Api

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, doc='/docs')

from src.controller.AuthController import auth as auth

api.add_namespace(auth)

app = Flask(__name__)
app.register_blueprint(blueprint)

app.run()
