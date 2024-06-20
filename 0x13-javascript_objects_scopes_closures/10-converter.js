#!/usr/bin/node
/* func that convert num from base 10 to another passed arg */
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
