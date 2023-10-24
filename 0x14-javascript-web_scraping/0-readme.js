#!/usr/bin/node
const fs = require('fs');

const filePath = process.argv[2];

fs.promises.readFile(filePath, 'utf8')
  .then((content) => {
    console.log(content);
  })
  .catch((error) => {
    console.log(error);
  });
