#!/usr/bin/python3
"""
    This script sends a POST request to the passed URL
    with the email as a parameter
"""

import requests
import sys
if __name__ == "__main__":
    value = {'email': sys.argv[2]}
    url = sys.argv[1]
    data = requests.post(url, data=valu)
    print(data.text)
