#!/usr/bin/node
/* script that prints a message depending of num oof arg */

const args = process.argv;

if (args.length <= 2) {
  console.log('No argument');
} else if (args.lenght === 3) {
  console.log('Arguments found');
} else {
  console.log('Arguments found');
}
