import requests
from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

from Utilities.settings import IP, user_id
from Requests.BasicCommands import send_actions, fetch_all_lights
from CustomObjects.Action import Action

from FlaskApp.Forms.NameForm import NameForm
from FlaskApp.Forms.LightToggleForm import LightToggleForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this is a really long hard to guess string lol'

bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    light_group = fetch_all_lights()
    form = NameForm()

    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('You just changed your name!')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('home'))

    return render_template('home.html', current_time=datetime.utcnow(), form=form, name=session.get('name'), lights=light_group)

@app.route('/lights', methods=['GET', 'POST'])
def lights():
    light_group = fetch_all_lights()
    form = LightToggleForm()
    form.selection.choices = light_group.lights

    if form.validate_on_submit():
        print('asldkfjhaslkjdfaslkdf')
        send_actions(Action(form.selection.data, on=True, bri=100))
        return redirect(url_for('home'))

    return render_template('home.html', form=form, current_time=datetime.utcnow(), lights=light_group)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/agent')
def agent():
    user_agent = request.headers.get('User-Agent')
    return f'<p>Your browser is {user_agent}'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('Errors/404.html')

@app.errorhandler(500)
def page_not_found(e):
    return render_template('Errors/500.html', error=e)

@app.route('/form')
def page_not_found():
    return render_template()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
