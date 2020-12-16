import requests
from time import sleep

from Utilities.settings import IP, user_id
from CustomObjects.Colour import Colour
from CustomObjects.Action import Action
from Requests.BasicCommands import send_actions, fetch_all_lights
import Requests.Effects as effects
from CustomObjects.LightGroup import LightGroup


lights = fetch_all_lights()

# effects.fade_between(lights, [Colour('red'), Colour('green')], brightness=100, fade_time=5)

for light in lights:
    send_actions(Action(light, on=True, colour=Colour('productivity')))
