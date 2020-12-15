import requests
from time import sleep

from Utilities.settings import IP, user_id
from Requests.get import fetch_all_lights
from CustomObjects.Colour import Colour
from CustomObjects.Action import Action
from Requests.BasicCommands import send_actions
import Requests.Effects as effects
from CustomObjects.LightGroup import LightGroup


lights = fetch_all_lights()

effects.flash_between(lights, [Colour('red'), Colour('blue')])
