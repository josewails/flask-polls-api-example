from datetime import datetime

from app.exts import db
from app.core.utils import generate_uuid


class Question(db.Model):
    id = db.Column(db.String(64), primary_key=True, default=generate_uuid)
    text = db.Column(db.String(1000), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __str__(self):
        return self.text
