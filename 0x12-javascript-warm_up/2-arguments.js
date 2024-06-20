#!/usr/bin/node
/* script that prints a message depending of num oof arg */

const args = process.argv;
const x = args.length;

if (x <= 2) {
  console.log('No argument');
} else if (x == 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
