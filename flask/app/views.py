import datetime

from flask import render_template, url_for, redirect
from flask.views import View

from app import app, db

from .forms import SignUp
from .models import User


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/show-template')
def show_template():
    return render_template("template.html")


@app.route('/current-time')
def current_time():
    now = datetime.datetime.now()
    day = now.strftime("%B %d, %Y")
    time = now.strftime("%I:%M %p")
    return 'It is now ' + time + ' on ' + day + '.'


class CurrentTimeTwo(View):

    def dispatch_request(self):
        now = datetime.datetime.now()
        day = now.strftime("%B %d, %Y")
        time = now.strftime("%I:%M %p")
        return 'It is now ' + time + ' on ' + day + '.'


app.add_url_rule('/current-time-two', view_func=CurrentTimeTwo.as_view(
    'current_time_two'))


@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUp()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    first_name=form.first_name.data,
                    last_name=form.last_name.data)
        db.session.add(user)
        db.session.commit()
        return 'Success!'
    return render_template('signup.html', form=form)
