#!/usr/bin/node
/* func that exec x time a func */
exports.callMeMoby = function (x, theFunction) {
  for (let y = 0; y < x; y++) {
    theFunction();
  }
};
