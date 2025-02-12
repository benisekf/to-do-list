from app import db
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(256), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    def __repr__(self):
        return f'<Task {self.description}>'
