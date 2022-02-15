from flask import request, Response
from flask_restful import Resource
from database.models import Notice

class NoticesApi(Resource):
    def get(self):
        notices = Notice.objects.all()
        return {'notices': [notice.to_json() for notice in notices]}

    def post(self):
        data = request.get_json()
        notice = Notice(**data)
        notice.save()
        return {'notice': notice.to_json()}

class NoticeApi(Resource):
    def delete(self, id):
        data = request.get_json()
        Notice.objects(id=data['id']).delete()
        return {'message': 'notice deleted'}
    
    def put(self, id):
        data = request.get_json()
        Notice.objects(id=data['id']).update(**data)
        return {'message': 'notice updated'}
    
    def get(self, id):
        notice = Notice.objects(id=id).to_json()
        return {'notice': notice.to_json()}