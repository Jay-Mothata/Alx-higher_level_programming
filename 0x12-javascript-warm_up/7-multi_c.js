#!/usr/bin/node

const numInput = parseInt(process.argv[2]);

if (!numInput) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numInput; i++) {
    console.log('C is fun');
  }
}
