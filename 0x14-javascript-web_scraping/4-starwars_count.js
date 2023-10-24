#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';

request.get(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const count = body.split("https://swapi-api.alx-tools.com/api/people/18").length - 1
    console.log(count)
  } else {
    console.error(error);
  }
});
