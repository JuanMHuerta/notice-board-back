from flask import Blueprint, request, Response
from database.models import Notice

notices = Blueprint('notices', __name__)

@notices.route('/notices', methods=['GET'])
def get_notices():
    notices = Notice.objects.all()
    return Response(notices.to_json(), mimetype='application/json', status=200)

@notices.route('/notices', methods=['POST'])
def create_notice():
    data = request.get_json()
    notice = Notice(
        title=data['title'],
        content=data['content']
    )
    notice.save()
    return Response(notice.to_json(), mimetype='application/json', status=201)

@notices.route('/notices/<notice_id>', methods=['GET'])
def get_notice(notice_id):
    notice = Notice.objects.get(id=notice_id)
    return Response(notice.to_json(), mimetype='application/json', status=200)

@notices.route('/notices/<notice_id>', methods=['PUT'])
def update_notice(notice_id):
    data = request.get_json()
    notice = Notice.objects.get(id=notice_id)
    notice.title = data['title']
    notice.content = data['content']
    notice.save()
    return Response(notice.to_json(), mimetype='application/json', status=200)

@notices.route('/notices/<notice_id>', methods=['DELETE'])
def delete_notice(notice_id):
    notice = Notice.objects.get(id=notice_id)
    notice.delete()
    return Response(status=204)