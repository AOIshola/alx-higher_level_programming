#!/usr/bin/node

const first = process.argv[2];
const second = process.argv[3];

function add (a, b) {
  a = parseInt(process.argv[2]);
  b = parseInt(process.argv[3]);

  if (!a || !b || isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    console.log(a + b);
  }
}

add(first, second);
