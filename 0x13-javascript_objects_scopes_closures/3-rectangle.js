#!/usr/bin/node

module.exports = class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print() {
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let k = 0; k < this.width; k++) {
        line += 'X';
      }
      console.log(line);
    }
  }
};
