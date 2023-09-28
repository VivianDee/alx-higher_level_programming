#!/bin/bash
# This script takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -slI -o /dev/null -w "%{http_code}" "$1"
