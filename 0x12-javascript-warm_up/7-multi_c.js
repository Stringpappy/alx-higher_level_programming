#!/usr/bin/node
const x = process.argv[2];

if (x === undefined || isNaN(parseInt(x))) {
  console.log('Missing number of occurrences');
} else {
  for (let y = 0; y < parseInt(x); y++) {
    console.log('C is Fun');
  }
}
