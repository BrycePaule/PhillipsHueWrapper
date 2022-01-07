import requests
from time import sleep
import upnpy

from Utilities.settings import IP
from Utilities.utils import roll
from CustomObjects.Colour import Colour
from CustomObjects.Action import Action
from Requests.BasicCommands import send_actions, fetch_all_lights, turn_off, turn_on
import Requests.Effects as effects
from CustomObjects.LightGroup import LightGroup

print(IP)


