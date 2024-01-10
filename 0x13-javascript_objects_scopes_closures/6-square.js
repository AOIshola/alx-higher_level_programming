#!/usr/bin/node

const pSquare = require('./5-square');

module.exports = class Square extends pSquare {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    let letter;
    if (!c) {
      letter = 'X';
    } else {
      letter = 'C';
    }
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let k = 0; k < this.width; k++) {
        line += letter;
      }
      console.log(line);
    }
  }
};
