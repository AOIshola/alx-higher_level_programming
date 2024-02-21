#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) throw error;
  const result = JSON.parse(body).reduce((acc, user) => {
    if (user.completed === true) {
      acc[user.userId] = (acc[user.userId] || 0) + 1;
    }
    return acc;
  }, {});
  console.log(result);
});
