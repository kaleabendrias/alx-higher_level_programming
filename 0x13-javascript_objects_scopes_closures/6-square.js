#!/usr/bin/node
// Square that defines a square and inherits from Square of 5-square.js

module.exports = class Square extends require('./5-square') {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let x = '';
      for (let j = 0; j < this.width; j++) {
        x += c;
      }
      console.log(x);
    }
  }
};
