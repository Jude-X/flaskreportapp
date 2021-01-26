from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Verticaluser(db.Model):
    __tablename__ = "verticalusers"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    vertical = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f"VerticalUser('{self.id}', '{self.email}', '{self.vertical}')"


class Appuser(db.Model):
    __tablename__ = "appusers"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    vertical = db.Column(db.String(30), nullable=False)
    image_file = db.Column(db.String(20), nullable=False,
                           default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"AppUser('{self.id}', '{self.email}''{self.vertical}')"
