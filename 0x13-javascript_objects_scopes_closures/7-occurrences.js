#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  const len = list.length;
  for (let x = 0; x < len; x++) {
    if (searchElement === list[x]) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};
