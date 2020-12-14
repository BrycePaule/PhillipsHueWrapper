import requests

from settings import IP, id_key


def lookup_light_params():
    response = requests.get(f'http://{IP}/api/{id_key}/lights')

    for _, values in response.json().items():
        print([val for val in values['state']])
        break


def lookup_lights():
    response = requests.get(f'http://{IP}/api/{id_key}/lights')

    for key, value in response.json().items():
        print(key, value)
