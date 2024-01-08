#!/usr/bin/node

const args = process.argv;
const argc = process.argv.length;
const arr = [];
let i = 2;

if (argc === 1 || argc === 0) {
  console.log(0);
}

while (i < argc) {
  const num = parseInt(args[i]);
  arr.push(num);
  i++;
}

const max2 = arr.sort();
console.log(max2[max2.length - 2]);
