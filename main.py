import json
import requests
from time import sleep

from settings import IP, id_key
from utils import clamp
from lookups import lookup_lights, lookup_light_params
from Colour import Colour


def get_lights():
    response = requests.get(f'http://{IP}/api/{id_key}/lights')

    for key, val in response.json().items():
        print(key, val)


def change_light(xy=None, brightness=None, transitiontime=None):
    data = {'on': True}

    if brightness:
        brightness = clamp(brightness, 0, 100)
        brightness = (254 // 100) * brightness
        data['bri'] = brightness

    if xy:
        data['xy'] = xy

    if transitiontime:
        data['transitiontime'] = transitiontime

    response = requests.put(f'http://{IP}/api/{id_key}/lights/2/state', json=data)
    print(response.json())


def turn_off():
    data = {'on': False}
    response = requests.put(f'http://{IP}/api/{id_key}/lights/2/state', json=data)
    print(response.json())


def turn_on():
    data = {'on': True}
    response = requests.put(f'http://{IP}/api/{id_key}/lights/2/state', json=data)
    print(response.json())


lookup_light_params()
# lookup_lights()

for colour in Colour.colour_maps:
    print(colour)
    transition_time = 2
    change_light(xy=Colour(colour).as_xy(), brightness=220, transitiontime=transition_time * 10)

    sleep(transition_time)

