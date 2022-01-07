from Utilities.utils import fetch_username
"""
    Get Hue Bridge IP
    https://discovery.meethue.com/
"""

# home
# IP = '192.168.1.22'

# remy
IP = '192.168.0.2'

user_id = fetch_username(IP)
