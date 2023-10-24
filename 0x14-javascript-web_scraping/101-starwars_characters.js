#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const link = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(link, (error, response, body) => {
  if (error) console.error(error);

  const data = JSON.parse(body);
  const characters = data.characters;

  characters.forEach((character) => {
    request(character, (charError, charResponse, charBody) => {
      if (charError) console.error(charError);

      const charData = JSON.parse(charBody);

      console.log(charData.name);
    });
  });
});
