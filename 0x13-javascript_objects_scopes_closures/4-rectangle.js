#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.width === 0 || this.height === 0) {
      console.log(' ');
    } else {
      for (let c = 0; c < this.height; c++) {
        const column = 'X'.repeat(this.width);
        console.log(column);
      }
    }
  }

  rotate () {
    if (this.width !== 0 && this.height !== 0) {
      const swap = this.width;
      this.width = this.height;
      this.height = swap;
    }
  }

  double () {
    if (this.width !== 0 && this.height !== 0) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}

module.exports = Rectangle;
