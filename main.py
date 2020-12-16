import requests
from time import sleep

from Utilities.settings import IP, user_id
from Utilities.utils import roll
from CustomObjects.Colour import Colour
from CustomObjects.Action import Action
from Requests.BasicCommands import send_actions, fetch_all_lights
import Requests.Effects as effects
from CustomObjects.LightGroup import LightGroup


lights = fetch_all_lights()

# effects.fade_between(lights, [Colour('red'), Colour('green'), Colour('blue')], fade_time=20, alternate_lights=True)

# for light in lights:
#     send_actions(Action(light, on=True, colour=Colour('productivity'), transition_time=0))

# effects.lava_lamp_warm(lights, speed=20)

effects.lava_lamp(lights, Colour('orange'), similarity_percent=10, transition_time=10)

