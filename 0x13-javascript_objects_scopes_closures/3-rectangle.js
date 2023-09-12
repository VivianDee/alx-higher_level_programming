#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let num = this.height;
    const myStr = 'X';
    while (num > 0) {
      console.log(myStr.repeat(this.width));
      num--;
    }
  }
};
