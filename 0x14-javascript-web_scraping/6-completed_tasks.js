#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err == null) {
    const the_rsp = {};
    const json = JSON.parse(body);
    for (let x = 0; x < json.length; x++) {
      if (json[x].completed === true) {
        if (the_rsp[json[x].serId] === undefined) {
          the_rsp[json[x].userId] = 0;
        }
        the_rsp[json[x].userId]++;
      }
    }
    console.log(the_rsp);
  }
});
