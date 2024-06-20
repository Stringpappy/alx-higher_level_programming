#!/usr/bin/node
/* script that searches the second biggest integer in the list of arguments. */
const num = process.argv;
const x = num.length;
if (x <= 3) {
  console.log('0');
} else {
  let sec = parseInt(num[2]);
  let h = parseInt(num[3]);
  for (let w = 2; w < x; w++) {
    const ku = parseInt(num[w]);
    if (ku > h) {
      sec = h;
      h = ku;
    } else if (ku > sec && ku < h) {
      sec = ku;
    }
    console.log(sec);
  }
}
