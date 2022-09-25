from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

from src.utils.Config import Config


# api
api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# db
db = SQLAlchemy()

# app
app = Flask(__name__)
app.register_blueprint(api_bp, url_prefix='/api')
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    from src.model.resume.Resume import Resume
    from src.model.user.User import User
    db.create_all()

# rotes
from src.controller.ResumeController import ResumeController
from src.controller.UserController import UserController

api.add_resource(UserController, '/users')
api.add_resource(ResumeController, '/resume')

# message consumer
from src.consumer.MessageConsumer import messageConsumer

messageConsumer.start()
