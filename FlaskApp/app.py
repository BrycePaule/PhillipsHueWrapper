import requests
from flask import Flask
from flask import render_template

from Utilities.settings import IP, user_id
from Requests.BasicCommands import send_actions, fetch_all_lights
from CustomObjects.Action import Action

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/lights')
def lights():
    lights = fetch_all_lights()
    send_actions(Action(lights[0], on=True, bri=100))
    return render_template('home.html')
    # return 'this is some text to be on the light page'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
