#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

request.get(`https://swapi-api.alx-tools.com/api/films/${id}`)
  .then(response => {
    console.log(response.data.title);
  })
  .catch(error => {
    console.log(error);
  });
