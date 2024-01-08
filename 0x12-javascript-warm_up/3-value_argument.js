#!/usr/bin/node

const args = process.argv;

let i = 0;
for (i = 0; args[i]; i++) {
  // pass
}

if (i === 2) {
  console.log('No argument');
} else {
  for (i = 2; args[i]; i++) {
    console.log(args[i]);
  }
}
