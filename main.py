import requests
from time import sleep

from Utilities.settings import IP, user_id
from Utilities.utils import roll
from CustomObjects.Colour import Colour
from CustomObjects.Action import Action
from Requests.BasicCommands import send_actions, fetch_all_lights
import Requests.Effects as effects
from CustomObjects.LightGroup import LightGroup

from FlaskApp.app import app

# light_group = fetch_all_lights()
# effects.lava_lamp(light_group, colour=Colour('relax'), similarity_percent=10, transition_time=5)

app.run(debug=True, host='0.0.0.0')