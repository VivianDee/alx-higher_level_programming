#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const link = 'https://swapi-api.alx-tools.com/api/films/' + id;

request(link, (error, response, body) => {
  if (error) console.error(error);

  const data = JSON.parse(body);
  console.log(data.title);
});
