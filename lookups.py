import requests

from settings import IP, user_id


def lookup_light_params():
    response = requests.get(f'http://{IP}/api/{user_id}/lights')

    for _, values in response.json().items():
        print([val for val in values['state']])
        break


def lookup_lights():
    response = requests.get(f'http://{IP}/api/{user_id}/lights')

    for key, value in response.json().items():
        print(key, value)
