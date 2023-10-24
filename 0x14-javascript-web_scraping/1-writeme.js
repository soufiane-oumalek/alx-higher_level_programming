#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];

fs.promises.writeFile(filePath, content, 'utf8')
  .then(() => {
    console.log('File has been written successfully.');
  })
  .catch((error) => {
    console.log(error);
  });
