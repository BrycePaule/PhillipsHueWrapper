from Utilities.utils import fetch_username
"""
    Get Hue Bridge IP
    https://discovery.meethue.com/
"""

IP_Lists = {
    "Home": '192.168.0.2',
    "Parents": '192.168.1.22'
}

SELECTION = "Home"

IP = IP_Lists[SELECTION]
# USER_ID = fetch_username(IP_Lists[SELECTION])
