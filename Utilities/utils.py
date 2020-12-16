import requests


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


def clamp(value, minimum, maximum):
    if value <= minimum:
        return minimum
    elif value >= maximum:
        return maximum
    else:
        return value





