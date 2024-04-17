#!/usr/bin/node

const lenArg = process.argv.length;

if (lenArg <= 2) console.log('No argument');
else if (lenArg === 3) console.log('Argument found');
else console.log('Arguments found');
