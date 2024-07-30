#!/usr/bin/node
const je = require('je');
je.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
