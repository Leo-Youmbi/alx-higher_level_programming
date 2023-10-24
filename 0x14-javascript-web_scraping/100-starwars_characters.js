#!/usr/bin/node
const request = require('request');
const URL = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;
request(URL, function (error, response, body) {
  if (error) console.log(error);
  for (const URL_CHAR of JSON.parse(body).characters) {
    request(URL_CHAR, (error, response, body) =>
      !error && console.log(JSON.parse(body).name));
  }
});
