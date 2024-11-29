from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie_reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

if __name__ == '__main__':
    with app.app_context():
        # Import models inside context
        from models import MovieReview
        db.create_all()
        # Import routes after models
        from routes import *
    app.run(debug=True)

