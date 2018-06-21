from app import app

from flask import render_template, flash, redirect, url_for

# import form the python file in apps/forms.py, use the LoginForm class
from app.forms import LoginForm


# These are called 'view functions' and define the bahaviour of different views, mapped by their route names.

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


# methods=[...] defines the available methods, default is only GET.
@app.route( '/login', methods=['GET', 'POST'] )
def login():
    form = LoginForm()
    # Pass the name of the html-defining file, the title as well as an instance 
    # of the class (form) which will be used in the html file.
    # form=form tells the render_template function that it has an internal variable named form,
    # to which the instance of the LoginForm called form is passed.

    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me{}'.format(
            form.username.data, form.remember_me.data ) )
        return redirect( url_for('index') )

    return render_template('login.html', title='Sign in', form=form)
