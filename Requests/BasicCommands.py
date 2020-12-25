import requests
from time import sleep

from Utilities.settings import IP, user_id
from CustomObjects.LightGroup import LightGroup
from CustomObjects.Light import Light


def fetch_all_lights():
    r = requests.get(f'http://{IP}/api/{user_id}/lights')
    return LightGroup([Light(light, r.json()[light]) for light in r.json()])

def turn_on(light):
    data = {'on': True}
    r = requests.put(f'http://{IP}/api/{user_id}/lights/{light}/state', json=data)
    print(f'{light}: {r.json()}')

def turn_off(light):
    data = {'on': False}
    r = requests.put(f'http://{IP}/api/{user_id}/lights/{light}/state', json=data)
    print(f'{light}: {r.json()}')

def colour_loop(light):
    data = {'effect': 'colorloop'}
    r = requests.put(f'http://{IP}/api/{user_id}/lights/{light}/state', json=data)
    print(f'{light}: {r.json()}')

def send_actions(actions):
    if type(actions) != list:
        actions = [actions]

    for action in actions:
        r = requests.put(f'http://{IP}/api/{user_id}/lights/{action.light.id}/state', json=action.as_dict())
        print(f'{action.light} --- {r.json()}')