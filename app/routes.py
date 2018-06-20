from app import app

from flask import render_template


@app.route('/')
@app.route('/index')
@app.route('/index2')
def index():
    user = {'user_one': 'Lord Lordsson'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'AHEAHUEAHe!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAa'
        }
    ]
    return render_template('index.html', title='Flaskus maximus', user=user, posts=posts)

