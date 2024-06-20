#!/usr/bin/node
/* script script that prints My number: <first argument converted in integer> */
const num = process.argv[2];

if (num === undefined || isNaN(parseInt(num))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(num));
}
