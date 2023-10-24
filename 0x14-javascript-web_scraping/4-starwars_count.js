#!/usr/bin/node
const request = require('request');
const api_url = process.argv[2]
request(api_url, function (error, response, body) {
  if (!error) {
    const rsult = JSON.parse(body).rsult;
    console.log(rsult.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
