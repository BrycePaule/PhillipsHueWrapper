import requests

from Utilities.settings import IP, user_id
from CustomObjects.Light import Light
from CustomObjects.LightGroup import LightGroup


def fetch_all_lights():
    r = requests.get(f'http://{IP}/api/{user_id}/lights')
    return LightGroup([Light(light, r.json()[light]) for light in r.json()])


# def all_lights_by_id():
#     r = requests.get(f'http://{IP}/api/{user_id}/lights')
#     return list(r.json().keys())
#
#
# def all_lights_by_name():
#     r = requests.get(f'http://{IP}/api/{user_id}/lights')
#     lights_raw = list(r.json().items())
#
#     lights = []
#     for light in lights_raw:
#         lights.append([light[1]['name'], light[0]])
#
#     return lights
