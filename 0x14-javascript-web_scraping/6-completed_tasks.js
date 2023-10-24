#!/usr/bin/node

const axios = require('request');
const url = process.argv[2];

request.get(url)
  .then(response => {
    const data = response.data;
    const results = {};

    for (const task of data) {
      if (task.completed) {
        results[task.userId] = (results[task.userId] || 0) + 1;
      }
    }
    console.log(results);
  })
  .catch(error => {
    console.log(error);
  });
