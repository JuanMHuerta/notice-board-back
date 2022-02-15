from .notices import NoticesApi, NoticeApi

def initialize_routes(api):
    api.add_resource(NoticesApi, '/api/v1/notices')
    api.add_resource(NoticeApi, '/api/v1/notices/<id>')