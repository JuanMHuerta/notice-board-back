from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class Notice(db.Document):
    title = db.StringField(max_length=255, required=True, unique=True)
    content = db.StringField(max_length=255, required=True)

class User(db.Document):
    email = db.StringField(max_length=255, required=True, unique=True)
    password = db.StringField(max_length=255, required=True, min_length=6)
    username = db.StringField(max_length=255, required=True, unique=True)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)