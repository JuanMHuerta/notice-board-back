from flask import Flask
from resources.notices import notices

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://mongo/notices'
}

initialize_db(app)
app.register_blueprint(notices, url_prefix='/api/v1/')

@app.route('/')
def hello():
    return {'hello': 'world'}

app.run(host='0.0.0.0')
