from flask import render_template, request, redirect, url_for
from app import app, db
from models import MovieReview

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    # Query all reviews from the database, ordered by time_created (newest first)
    reviews = MovieReview.query.order_by(MovieReview.time_created.desc()).all()
    return render_template('data.html', reviews=reviews)

@app.route('/add_review', methods=['GET', 'POST'])
def add_review():
    if request.method == 'POST':
        new_review = MovieReview(
            movie_name=request.form['movie_name'],
            review=request.form['review'],
            rating=float(request.form['rating'])
        )
        
        db.session.add(new_review)
        db.session.commit()
        
        # Change redirect to data page instead of index
        return redirect(url_for('data'))
    
    return render_template('add_review.html')

