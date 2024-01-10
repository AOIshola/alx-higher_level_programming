#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let noOfOccurences = 0;
  let i = 0;

  while (i < list.length) {
    if (list[i] === searchElement) {
      noOfOccurences++;
    }
    i++;
  }

  return (noOfOccurences);
};
