from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    avatar = db.Column(db.String(200))
    twitter = db.Column(db.String(100))
    phoneNumber = db.Column(db.String(20))
    notes = db.Column(db.Text)
    favorite = db.Column(db.Boolean, default=False)

    def print(self):
        return {
            'id': self.id,
            'name': self.name,
            'avatar': self.avatar,
            'twitter': self.twitter,
            'phoneNumber': self.phoneNumber,
            'email': self.email,
            'notes': self.notes,
            'favorite': self.favorite
        }
