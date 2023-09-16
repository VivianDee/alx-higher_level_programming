#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (c) {
    let num = this.height;
    let myStr = 'X';
    if (c) {
      myStr = c;
    }
    while (num > 0) {
      console.log(myStr.repeat(this.width));
      num--;
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
