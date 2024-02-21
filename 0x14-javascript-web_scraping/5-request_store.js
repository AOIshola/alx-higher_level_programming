#!/usr/bin/node

const fs = require('fs');
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) throw error;
  fs.writeFile(process.argv[3], body, { encoding: 'utf-8' }, (err) => {
    if (err) {
      throw err;
    }
  });
});
