from app.models.database import db


class Workout(db.Model):

    __tablename__ = "workouts"

    workout_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)
    exercise_id = db.Column(
        db.Integer, db.ForeignKey("exercises.exercise_id"), nullable=False
    )
    title = db.Column(db.String(255), nullable=True)
    start_time = db.Column(db.DateTime, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    calories = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, exercise_id, start_time, duration, calories, **kwargs):
        self.user_id = user_id
        self.exercise_id = exercise_id
        self.start_time = start_time
        self.duration = duration
        self.calories = calories

        if "title" in kwargs:
            self.title = kwargs["title"]

    def __repr__(self):
        return f"<Workout workout_id={self.workout_id} title={self.title}>"
