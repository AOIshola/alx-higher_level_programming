#!/usr/bin/node

const request = require('request');

function getTitle () {
  const endpoint = process.argv[2];
  request(endpoint, (error, response, body) => {
    if (error) {
      console.log(error.message);
    }
    const movieData = JSON.parse(body);
    //    const title = movieData.title;
    const results = movieData.results;
    const objs = results.reduce((acc, obj) => {
      const count = obj.characters.reduce((acc, url) => {
        const tokens = url.split('/');

        if (tokens[tokens.length - 2] === '18') {
          return acc + 1;
        } else {
          return acc;
        }
      }, 0);
      return count + acc;
    }, 0);
    console.log(`${objs}`);
  });
}

getTitle();
