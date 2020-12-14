import requests

from Utilities.settings import IP, user_id


def all_lights():
    r = requests.get(f'http://{IP}/api/{user_id}/lights')
    return list(r.json().items())


def all_lights_by_id():
    r = requests.get(f'http://{IP}/api/{user_id}/lights')
    return list(r.json().keys())


def all_lights_by_name():
    r = requests.get(f'http://{IP}/api/{user_id}/lights')
    lights_raw = list(r.json().items())

    lights = []
    for light in lights_raw:
        lights.append([light[1]['name'], light[0]])

    return lights
