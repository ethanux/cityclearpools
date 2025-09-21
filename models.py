from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(100), nullable=False)
    ptype = db.Column(db.String(100),nullable=False)
    comment = db.Column(db.String(200), nullable=True)


    def __repr__(self):
        return f'<Project {self.id} {self.ptype} >'
