#!/usr/bin/node
const my  = require('my');
my.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
