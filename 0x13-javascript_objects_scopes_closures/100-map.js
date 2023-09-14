#!/usr/bin/node
const mList = require('./100-data').list;
console.log(mList);
console.log(mList.map((c, i) => c * i));