from flask import Flask
from app.models.database import connect_to_db

app = Flask(__name__)
app.secret_key = "MySecretKey"

connect_to_db(app)

# Import the models after initializing the SQLAlchemy instance
from app.models import User

# Import the routes after importing the models
from app import routes