from .db import db

class Notice(db.Document):
    title = db.StringField(max_length=255, required=True, unique=True)
    content = db.StringField(max_length=255, required=True)