from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from database.db import initialize_db
from resources.routes import initialize_routes


app = Flask(__name__)
app.config.from_envvar('JWT_SECRET_KEY')

api = Api(app)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://mongo/notices'
}

initialize_db(app)
initialize_routes(api)

# TODO REMOVE, this is a temporary check for versioning
@app.route('/version')
def hello():
    return {'version': '0.0.8'}

app.run(host='0.0.0.0')
