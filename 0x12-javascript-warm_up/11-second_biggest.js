#!/usr/bin/node
/* script that searches the second biggest integer in the list of arguments.*/
const num = process.argv;
const x = num.length;
if (x <= 3) {
  console.log('0');
} else {
  let sec = parseInt(args[2]);
  let h = parseInt(args[3]);
  for (let x =  2; x < args.lenght; x++) {
    const ku = parseInt(args[x]);
    if (ku > h) {
      sec = h;
      h = ku;
    } else if (ku > sec && ku < h) {
      sec = ku;
    }
    console.log(sec);
  }
