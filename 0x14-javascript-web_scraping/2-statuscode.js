#!/usr/bin/node
const request = require('request-promise');
const url = process.argv[2];
request(url)
  .then(response => {
    console.log(`code: ${response.statusCode}`);
  })
  .catch(error => {
    console.log(`code: ${error.statusCode}`);
  });
