from flask import render_template
from app import app
from .request import get_news

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_news = get_news('popular')
    print(popular_news)
    title = 'news1234.com'
    return render_template('index.html', title = title,popular = popular_news)


# Views
@app.route('/')
def news():

    '''
    View movie page function that returns the movie details page and its data
    '''

    title = 'news1234.com'
    return render_template('index.html',title = title)
