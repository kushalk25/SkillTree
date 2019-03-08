from flask import render_template
from flask import request
from app import app

@app.route('/')
@app.route('/index')
def index():
    skills = [ 'Soccer', 'Guitar', 'Cooking', 'Workouts' ]
    return render_template('index.html', skills=skills)
