from app.models.database import db


class User(db.Model):
    """Model definition of a user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(255), nullable=True)
    gender = db.Column(db.String(20), nullable=True)
    weight = db.Column(db.Integer, nullable=True)
    body_fat = db.Column(db.Float, nullable=True)
    height = db.Column(db.Integer, nullable=True)
    birthday = db.Column(db.DateTime, nullable=True)

    workouts = db.relationship("Workout", backref="user", lazy=True)

    def __init__(self, email, password, **kwargs):
        self.email = email
        self.password = password

        if "name" in kwargs:
            self.name = kwargs["name"]

        if "gender" in kwargs:
            self.gender = kwargs["gender"]

        if "weight" in kwargs:
            self.weight = kwargs["weight"]

        if "body_fat" in kwargs:
            self.body_fat = kwargs["body_fat"]

        if "height" in kwargs:
            self.height = kwargs["height"]

        if "birthday" in kwargs:
            self.height = kwargs["birthday"]

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"
