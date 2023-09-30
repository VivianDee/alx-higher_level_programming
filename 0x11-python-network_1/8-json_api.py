#!/usr/bin/python3
"""
    This script sends a POST request to the passed URL
    with a letter as a parameter
"""

import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) == 2:
        val = sys.argv[1]
    else:
        val = ''
    value = {'q': val}
    url = 'http://0.0.0.0:5000/search_user'
    data = requests.post(url, data=value)
    try:
        to_json = data.json()
        if to_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(to_json['id'], to_json['name']))
    except Exception:
        print("Not a valid JSON")
