#!/usr/bin/node
const Sq = require('./5-square');

module.exports = class Square extends Sq {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      this.print(c);
    }
  }
};
