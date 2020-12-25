import requests
import random


""" HUE BRIDGE INTERACTION"""

def fetch_username(IP):
    data = {"devicetype": "my_hue_app#bryce"}

    r = requests.get(f'http://{IP}/api', json=data)
    if r.status_code == 200:
        print('Established known connection to Phillips Hue Hub.')
        return load_username()

    r = requests.post(f'http://{IP}/api', json=data)

    if 'error' in r.json()[0]:
        raise Exception(f'{r.json()[0]["error"]["description"]}')

    username = r.json()[0]['success']['username']
    save_username(username)
    print('Established new connection to Phillips Hue Hub.')
    return username

def save_username(string):
    with open('username.txt', 'w') as f:
        f.write(string)

def load_username():
    with open('username.txt', 'r') as f:
        username = f.read().strip()
    if username:
        return username

""" HELPER FUNCTIONS """

def clamp(value, minimum, maximum):
    if value <= minimum:
        return minimum
    elif value >= maximum:
        return maximum
    else:
        return value

def increment_index(index, cap, count=1):
    return (index + count) % cap

def offset_colour_channel(val, percentage_offset):
    if type(percentage_offset) is int:
        percentage_offset /= 100
    offset = int(255 * percentage_offset)
    return clamp(val + random.randint(-offset, offset), 0, 255)

def offset_val_by_percentage(val, percentage_offset, clamp_val=False, lower=0, upper=0):
    if type(percentage_offset) is int:
        percentage_offset /= 100

    offset = int(val * percentage_offset)

    if clamp_val and not lower and not upper:
        raise Exception('Please input valid clamp boundaries.')

    if clamp_val:
        return clamp(val + random.randint(-offset, offset), lower, upper)
    else:
        return val + random.randint(-offset, offset)

def roll(chance):
    outcome = random.randint(0, 100)
    return outcome <= chance





