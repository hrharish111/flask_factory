from apps import api
from apps.auth_app import view

namespace = api.namespace('auth', description=' user auth info')

namespace.add_resource(view.UserInfo,"/login")