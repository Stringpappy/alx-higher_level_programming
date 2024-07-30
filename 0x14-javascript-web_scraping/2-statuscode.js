#!/usr/bin/node
const myrequest = require('myrequest');
myrequest.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
