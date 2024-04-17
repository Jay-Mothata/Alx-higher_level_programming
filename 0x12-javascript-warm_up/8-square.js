#!/usr/bin/node

const squareSize = parseInt(process.argv[2], 10);

if (!squareSize) console.log('Missing size');
else {
  for (let i = 0; i < squareSize; i++) {
    let square = '';
    for (let j = 0; j < squareSize; j++) {
      square += 'X';
    }
    console.log(square);
  }
}
