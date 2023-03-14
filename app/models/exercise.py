from app.models.database import db


class Exercise(db.Model):

    __tablename__ = "exercises"

    exercise_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    muscle = db.Column(db.String(255), nullable=False)
    difficulty = db.Column(db.String(255), nullable=False)
    equipment = db.Column(db.String(255), nullable=False)
    instructions = db.Column(db.String(1000), nullable=False)

    workouts = db.relationship("Workout", backref="exercise", lazy=True)

    def __repr__(self):
        return f"<Exercise exercise_id={self.exercise_id} name={self.name}>"
