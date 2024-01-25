#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the http response
response=$(curl -s -i -o /dev/null -w "%{http_code}" $1); [ $response -eq 200 ] && curl -s $1 || echo ""
