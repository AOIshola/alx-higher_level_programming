#!/usr/bin/node

const externalList = require('./100-data').list;

console.log(externalList);
console.log(externalList.map((item, idx) => (item * idx)));
