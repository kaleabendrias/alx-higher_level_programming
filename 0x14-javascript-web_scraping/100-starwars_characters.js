#!/usr/bin/node
const request = require('request');
const util = require('util');
const promisifiedRequestGet = util.promisify(request.get);

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/';

async function getCharacters() {
    try {
        const { body } = await promisifiedRequestGet(url + id);
        const data = JSON.parse(body);
        const characters = data.characters;
        for (const characterUrl of characters) {
            try {
                const characterData = await promisifiedRequestGet(characterUrl);
                console.log(JSON.parse(characterData.body).name);
            } catch (err) {
                console.error(err);
            }
        }
    } catch (err) {
        console.error(err);
    }
}

getCharacters();
