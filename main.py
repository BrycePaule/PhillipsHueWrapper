import requests
from time import sleep

from Utilities.settings import IP, user_id
from Requests.get import all_lights, all_lights_by_id, all_lights_by_name
from Wrappers.Colour import Colour
from Wrappers.Action import Action
from Requests.BasicCommands import send_actions
import Requests.Effects as effects


# for light in all_lights_by_id():
#     send_actions([
#         Action(light, on=True, colour=Colour('red')),
#         Action(light, colour=Colour('blue')),
#         Action(light, colour=Colour('green')),
#         Action(light, colour=Colour('yellow')),
#         Action(light, colour=Colour('pink')),
#         Action(light, colour=Colour('light_blue')),
#     ], fill_time=1)

colours = [Colour('red'), Colour('green'), Colour('blue')]
# effects.flash([2], Colour('pink'), 0.4)


send_actions([Action(2, bri=30, colour=Colour((255, 80, 0)))])