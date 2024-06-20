#!/usr/bin/node
/* script that prints a square  */
const size = process.argv[2];

if (size === undefined || isNaN(parseInt(size))) {
  console.log('Missing size');
} else {
  for (let y = 0; y < parseInt(size); y++) {
    let row = '';
    for (let z = 0; z < parseInt(size); z++) {
      row += 'X';
    }
    console.log(row);
  }
}
