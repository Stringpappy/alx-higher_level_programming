#!/usr/bin/node
/* script that computes and prints a factorial */

let args = parseInt(process.argv[2]);

if (isNaN(args)) {
  args = 1;
}

function factorial (num) {
  if (num === 1) {
    return 1;
  }
  return num * factorial(num - 1);
}
console.log(factorial(args));
