#!/usr/bin/python3
"""This script fetches https://alx-intranet.hbtn.io/status"""

import requests
if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    data = requests.get(url)
    print("Body response:")
    print("\t- type: {}\n\t- content: {}"
          .format(type(data.text), data.text))
