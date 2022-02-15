from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://mongo/notices'
}

initialize_db(app)
initialize_routes(api)

@app.route('/')
def hello():
    return {'version': '0.0.6'}

app.run(host='0.0.0.0')
