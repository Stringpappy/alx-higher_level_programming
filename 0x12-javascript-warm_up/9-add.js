#!/usr/bin/node
/* script that add int */
const f = process.argv[2];
const s = process.argv[3];

function add (a, b) {
  return a + b;
}

const a = parseInt(f);
const b = parseInt(s);
console.log(add(a, b));
