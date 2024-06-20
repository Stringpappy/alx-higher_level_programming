#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let y = 0; y < this.height; y++) {
      let d = '';
      for (let z = 0; z < this.width; z++) {
        d += c;
      }
      console.log(d);
    }
  }
}

module.exports = Square;
