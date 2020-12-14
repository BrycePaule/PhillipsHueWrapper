import json
import requests
from time import sleep

from settings import IP, user_id
from utils import clamp
from lookups import lookup_lights, lookup_light_params
from Colour import Colour
from Action import Action


def get_lights():
    response = requests.get(f'http://{IP}/api/{user_id}/lights')

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

    response = requests.put(f'http://{IP}/api/{user_id}/lights/2/state', json=data)
    print(response.json())


def send_actions(actions, fill_time=1.5):
    if type(actions) != list:
        r = requests.put(f'http://{IP}/api/{user_id}/lights/{actions.light_id}/state', json=actions.as_dict())
        print(r.json())

    else:
        for action in actions:
            r = requests.put(f'http://{IP}/api/{user_id}/lights/{action.light_id}/state', json=action.as_dict())
            print(r.json())

            if action.transitiontime:
                sleep(max(fill_time, action.transitiontime))
            else:
                sleep(fill_time)

def turn_off():
    data = {'on': False}
    response = requests.put(f'http://{IP}/api/{user_id}/lights/2/state', json=data)
    print(response.json())


def turn_on():
    data = {'on': True}
    response = requests.put(f'http://{IP}/api/{user_id}/lights/2/state', json=data)
    print(response.json())


def colour_loop():
    data = {'effect': 'colorloop'}
    response = requests.put(f'http://{IP}/api/{user_id}/lights/2/state', json=data)
    print(response.json())


lookup_light_params()
# lookup_lights()

send_actions([
    Action(2, on=True, colour=Colour('red')),
    Action(2, colour=Colour('blue')),
    Action(2, colour=Colour('green'), transition_time=3),
    Action(2, colour=Colour('yellow')),
    Action(2, colour=Colour('pink')),
    Action(2, colour=Colour('light_blue')),
], fill_time=1)