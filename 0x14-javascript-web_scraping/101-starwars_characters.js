#!/usr/bin/node
const request = require('request');
const util = require('util');
const id = process.argv[2];
const promisifiedRequest = util.promisify(request.get);

const url = 'https://swapi-api.hbtn.io/api/films/';

(async () => {
  try {
    const body = (await promisifiedRequest(url + id)).body;
    const film = JSON.parse(body);
    for (const characterUrl of film.characters) {
      try {
        const characterBody = (await promisifiedRequest(characterUrl)).body;
        const character = JSON.parse(characterBody);
        console.log(character.name);
      } catch (err) {
        console.error(err);
      }
    }
  } catch (err) {
    console.error(err);
  }
})();
