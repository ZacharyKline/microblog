from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Zachary'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Everything you know is a lie!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Eat the rich!'
        },
        {
            'author': {'username': 'Johnny Rico'},
            'body': 'The only good bug, is a dead bug!'
        },
        {
            'author': {'username': 'Your Mom'},
            'body': 'I love you very much, call me more.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
