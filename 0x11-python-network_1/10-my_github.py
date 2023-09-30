#!/usr/bin/python3
"""Uses the GitHub API to display a GitHub ID based on given credentials."""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    data = requests.get("https://api.github.com/user", auth=auth)
    try:
        print(data.json()["id"])
    except Exception:
        print("None")
