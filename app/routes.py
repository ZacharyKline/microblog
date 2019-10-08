from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
