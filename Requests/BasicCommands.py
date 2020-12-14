import requests
from time import sleep

from Utilities.settings import IP, user_id


def turn_on(light_id):
    data = {'on': True}
    response = requests.put(f'http://{IP}/api/{user_id}/lights/{light_id}/state', json=data)
    print(response.json())


def turn_off(light_id):
    data = {'on': False}
    response = requests.put(f'http://{IP}/api/{user_id}/lights/{light_id}/state', json=data)
    print(response.json())


def colour_loop(light_id):
    data = {'effect': 'colorloop'}
    response = requests.put(f'http://{IP}/api/{user_id}/lights/{light_id}/state', json=data)
    print(response.json())


def send_actions(actions):
    if type(actions) != list:
        r = requests.put(f'http://{IP}/api/{user_id}/lights/{actions.light_id}/state', json=actions.as_dict())
        print(r.json())

    else:
        for action in actions:
            r = requests.put(f'http://{IP}/api/{user_id}/lights/{action.light_id}/state', json=action.as_dict())
            print(r.json())

            if action.transitiontime:
                sleep(action.transitiontime * 10)
