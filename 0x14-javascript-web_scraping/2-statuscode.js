#!/usr/bin/node

const request = require("request");

response = request.get(process.argv[2])
console.log(response.statusCode)
