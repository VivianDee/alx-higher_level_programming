#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const link = process.argv[2];
const filePath = process.argv[3];

request(link, (error, response, body) => {
  if (error) console.error(error);

  const data = body;

  fs.writeFile(filePath, data, 'utf8', (error) => {
    if (error) throw error;
  });
});
