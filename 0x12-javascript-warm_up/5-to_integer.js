#!/usr/bin/node

const args = process.argv;

const number = parseInt(args[2]);
if (!args[2] || isNaN(number)) {
  console.log('Not a Number');
} else {
  console.log(number);
}
