#!/usr/bin/node
exports.esrever = function (list) {
  let rl = list.length - 1;
  let x = 0;
  while ((rl - x) > 0) {
    const atmp = list[rl];
    list[rl] = list[x];
    list[x] = atmp;
    x++;
    rl--;
  }
  return list;
};
