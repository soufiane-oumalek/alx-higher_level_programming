#!/usr/bin/node

if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const C = Number(process.argv[2]);
  let i = 0;
  while (i < C) {
    console.log("C".repeat(C));
    i++;
  }
}
