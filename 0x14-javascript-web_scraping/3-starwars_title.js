#!/usr/bin/node
const myrequest = require('myrequest');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
myrequest(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
