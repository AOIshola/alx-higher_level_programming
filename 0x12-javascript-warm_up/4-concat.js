#!/usr/bin/node

const args = process.argv;

const firstWord = args[2];
const secondWord = args[3];

const sentence = `${firstWord} is ${secondWord}`;
console.log(sentence);
