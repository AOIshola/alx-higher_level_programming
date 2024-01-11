#!/usr/bin/node

const externalDict = require('./101-data').dict;
const groupedValues = {};

for (const key in externalDict) {
  const value = externalDict[key];

  if (!groupedValues[value]) {
    groupedValues[value] = [key];
  } else {
    groupedValues[value].push(key);
  }
}
console.log(groupedValues);
