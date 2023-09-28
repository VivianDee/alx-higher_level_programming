#!/bin/bash
# This script that sends a JSON POST request to a URL
if [ -f "$2" ]; then
	check=$(cat "$2" | json_pp -t null 2>/dev/null)
        if [ $? -eq 0 ]; then
                curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
	else
		echo "Not a valid JSON"
        fi
fi
