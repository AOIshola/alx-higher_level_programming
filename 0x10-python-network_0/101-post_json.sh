#!/bin/bash
# sends a JSON POST request to a URL passed as the first argument, and displays the body of the response
curl -s -X POST -d @"$2" -H "content-type: application/json" $1
