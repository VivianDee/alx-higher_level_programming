#!/usr/bin/node

const request = require('request');
const link = process.argv[2];

request(link, (error, response, body) => {
  if (error) console.error(error);

  const data = JSON.parse(body);
  const count = data.count;
  const result = data.results;
  let num = 0;
  let character = '';

  for (let i = 0; i < count; i++) {
    character = 'https://swapi-api.alx-tools.com/api/people/18/';
    if (result[i].characters.includes(character)) {
      num += 1;
    }
  }
  console.log(num);
});
