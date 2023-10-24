#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';

request.get(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    let count = 0;
    data.results.forEach(film => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        count++;
      }
    });
    console.log(count);
  } else {
    console.error(error);
  }
});
