from flask import Blueprint
from apps.auth_app import view
from flask_restplus import Api

auth_blueprint = Blueprint("auth",__name__,url_prefix="/auth")
api = Api(auth_blueprint)
api.add_resource(view.UserInfo,"/test")