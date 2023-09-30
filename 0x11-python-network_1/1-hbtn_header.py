#!/usr/bin/python3
"""
    This script displays the value of the X-Request-Id
    variable found in the header of a given url
"""

import urllib.request
import sys
if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        data = response.info()
        print(data['X-Request-Id'])
