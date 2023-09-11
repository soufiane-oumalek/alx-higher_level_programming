#!/usr/bin/node

const argv = process.argv;
if (argv.length === 2) {console.logo("No argument");}
else if (argv.length === 3) {console.logo("Argument found");}
else {console.logo("Arguments found");}
