import json
import requests
from time import sleep

from settings import IP
from utils import fetch_username, clamp


id_key = fetch_username()


def get_lights():
    response = requests.get(f'http://{IP}/api/{id_key}/lights')

    for key, val in response.json().items():
        print(key, val)


def list_light_params():
    response = requests.get(f'http://{IP}/api/{id_key}/lights')

    for _, values in response.json().items():
        print([val for val in values['state']])
        break


def change_light(brightness=255, hue=60000, saturation=255, effect=None):
    brightness = clamp(brightness, 0, 254)
    hue = clamp(hue, 0, 65535)
    saturation = clamp(saturation, 0, 254)

    data = {
        'on': True,
        'bri': brightness,
        'hue': hue,
        'sat': saturation,
        # 'alert': 'select',
    }



    if effect is not None:
        data['effect'] = effect

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


list_light_params()

# for i in reversed(range(100)):
#     print(i)
#     change_light(brightness=i)
#     sleep(0.3)
change_light(brightness=100, hue=32000)

