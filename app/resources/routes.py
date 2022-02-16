from .notices import NoticesApi, NoticeApi
from .auth import AuthApi, LoginApi

def initialize_routes(api):
    api.add_resource(NoticesApi, '/api/v1/notices')
    api.add_resource(NoticeApi, '/api/v1/notices/<id>')

    api.add_resource(AuthApi, '/api/v1/auth')
    api.add_resource(LoginApi, '/api/v1/login')