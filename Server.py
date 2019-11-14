from flask import Flask, Blueprint
from flask_restplus import Api

blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint, doc='/docs')

from app.controller.AuthController import auth as auth

api.add_namespace(auth)

app = Flask(__name__)
app.register_blueprint(blueprint)

app.run(debug=True)

#blueprint = Blueprint('api', __name__, url_prefix='/api/')
#
#api = Api(blueprint)

#from app.controller.HelloController import HelloController


#@ns.route('/hello')
#class HelloWorld(Resource):
#    def get(self):
#        return {'hello': 'world'}
#
#if __name__ == '__main__':
#    app.run(debug=True)