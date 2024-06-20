#!/usr/bin/node
/* script that searches the second biggest integer in the list of arguments. */
const args = process.argv;
const x = args.length;

if (x <= 3) {
  console.log('0');
} else {
  let sec = parseInt(args[2]);
  let h = parseInt(args[3]);
  for (let y = 2; y < x; y++) {
    const kon = parseInt(args[y]);
    if (kon > h) {
      sec = h;
      h = kon;
    } else if (kon > sec && kon < h) {
      sec = kon;
    }
  }
  console.log(sec);
}
