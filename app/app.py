from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Notice

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://mongo/notices'
}

initialize_db(app)

@app.route('/')
def hello():
    return {'hello': 'world5'}

@app.route('/notices', methods=['GET'])
def get_notices():
    notices = Notice.objects.all()
    return Response(notices.to_json(), mimetype='application/json', status=200)

@app.route('/notices', methods=['POST'])
def create_notice():
    data = request.get_json()
    notice = Notice(
        title=data['title'],
        content=data['content']
    )
    notice.save()
    return Response(notice.to_json(), mimetype='application/json', status=201)

@app.route('/notices/<notice_id>', methods=['GET'])
def get_notice(notice_id):
    notice = Notice.objects.get(id=notice_id)
    return Response(notice.to_json(), mimetype='application/json', status=200)

@app.route('/notices/<notice_id>', methods=['PUT'])
def update_notice(notice_id):
    data = request.get_json()
    notice = Notice.objects.get(id=notice_id)
    notice.title = data['title']
    notice.content = data['content']
    notice.save()
    return Response(notice.to_json(), mimetype='application/json', status=200)

@app.route('/notices/<notice_id>', methods=['DELETE'])
def delete_notice(notice_id):
    notice = Notice.objects.get(id=notice_id)
    notice.delete()
    return Response(status=204)

notice = Notice(
    title='test',
    content='test'
)
notice.save()
print(Notice.objects.all())
app.run(host='0.0.0.0')
