from todo_list import db
from datetime import datetime
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now())
    def __repr__(self):
        return f"{self.id} - {self.content}"