#!/usr/bin/node

const args = process.argv;

function secondMax (arr) {
  const argc = arr.length;
  let i = 2;
  if (argc <= 2 || argc <= 3) {
    return (0);
  }

  const newArr = [];
  while (i < argc) {
    const num = parseInt(arr[i]);
    newArr.push(num);
    i++;
  }

  const max2 = newArr.sort((a, b) => a - b);
  return (max2[max2.length - 2]);
}

console.log(secondMax(args));
