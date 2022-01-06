import requests
from time import sleep
import upnpy

from Utilities.settings import IP, user_id
from Utilities.utils import roll
from CustomObjects.Colour import Colour
from CustomObjects.Action import Action
from Requests.BasicCommands import send_actions, fetch_all_lights, turn_off, turn_on
import Requests.Effects as effects
from CustomObjects.LightGroup import LightGroup

light_group = fetch_all_lights()
while True:
    effects.random_party(light_group)

# effects.lava_lamp(light_group, colour=Colour('relax'), similarity_percent=10, transition_time=5)

# for light in light_group:
#     turn_off(light.id)

# app.run(debug=True, host='0.0.0.0')

# print(light_group)
#
# upnp = upnpy.UPnP()
# devices = upnp.discover()
#
# print(devices)