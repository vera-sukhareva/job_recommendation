from flask import Flask, Blueprint
from flask_restful import Api

from src.consumer.MessageConsumer import messageConsumer
from src.controller.ResumeController import ResumeController
from src.controller.UserController import UserController

# api
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# app
app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix='/api')

# rotes
api.add_resource(UserController, '/users')
api.add_resource(ResumeController, '/resume')

messageConsumer.start()