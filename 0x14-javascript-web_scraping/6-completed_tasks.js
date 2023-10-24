#!/usr/bin/node

const axios = require('axios');
const url = process.argv[2];

axios.get(url)
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
