#!/bin/bash
# This script takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sI "$1" | grep "HTTP" | tail -n 1 | cut -d " " -f 2
