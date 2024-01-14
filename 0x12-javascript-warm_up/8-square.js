#!/usr/bin/node

const size = parseInt(process.argv[2]);
let i = 0;

if (!size || isNaN(size)) {
  console.log('Missing size');
}
for (i = 0; i < size; i++) {
  let line = '';
  for (let k = 0; k < size; k++) {
    line += 'X';
  }
  console.log(line);
}
