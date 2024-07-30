#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err == null) {
    const thersp = {};
    const json = JSON.parse(body);
    for (let x = 0; x < json.length; x++) {
      if (json[x].completed === true) {
        if (thersp[json[x].serId] === undefined) {
          thersp[json[x].userId] = 0;
        }
        thersp[json[x].userId]++;
      }
    }
    console.log(thersp);
  }
});
