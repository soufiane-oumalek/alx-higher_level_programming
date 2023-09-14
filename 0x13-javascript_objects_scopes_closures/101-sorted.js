#!/usr/bin/node
const dict = require('./101-data.js').dict;
const nDict = {};
for (const ky in dict) {
  if (nDict[dict[ky]] === undefined) {
    nDict[dict[ky]] = [];
  }
  nDict[dict[ky]].push(ky);
}
console.log(nDict);
