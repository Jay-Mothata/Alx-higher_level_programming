#!/usr/bin/node

const arrayLen = process.argv.length;

if (arrayLen === 2 || arrayLen === 3) {
  console.log('NaN');
} else {
  add(parseInt(process.argv[2]), parseInt(process.argv[3]));
}

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}
