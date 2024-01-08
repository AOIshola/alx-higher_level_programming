#!/usr/bin/node

const args = process.argv;

let i = 0;
let k = 0;
for (i = 0; args[i]; i++) {
  // pass
}

if (i === 2) {
  console.log('No argument');
} else {
  for (k = 2; k < i; k++) {
    console.log(args[k]);
  }
}
