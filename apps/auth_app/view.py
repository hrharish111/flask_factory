from apps.auth_app.model import User
from flask_restplus import Resource
from apps import db

class UserInfo(Resource):
    def get(self):
        admin = User(username='admin', email='admin@example.com')
        db.session.add(admin)
        db.session.commit()
        return "test works"



