#!/usr/bin/node

const xTime = parseInt(process.argv[2]);
let i = 0;

if (!xTime || isNaN(xTime)) {
  console.log('Missing number of occurrences');
} else {
  while (i < xTime) {
    console.log('C is fun');
    i++;
  }
}
