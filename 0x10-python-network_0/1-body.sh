#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of the response
status=$(curl -sI "$1" | grep "HTTP" | cut -d " " -f 2)
if [[ $status -eq 200 ]]; then
	curl -sL "$1"
fi
