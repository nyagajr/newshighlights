from flask import render_template
from app import app

# Views
@app.route('/')
def news():

    '''
    View movie page function that returns the movie details page and its data
    '''

    title = 'news1234.com'
    return render_template('index.html',title = title)
