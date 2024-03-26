#!/usr/bin/node

const request = require('request');

function getTitle () {
  const endpoint = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;
  request(endpoint, (error, response, body) => {
    if (error) {
      console.log(error.message);
    }
    const movieData = JSON.parse(body);
    const title = movieData.title;
    console.log(title);
  });
}

getTitle();
