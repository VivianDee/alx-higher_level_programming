#!/usr/bin/node

const request = require('request');

const link = process.argv[2];

request(link, (error, response, body) => {
  if (error) {
    console.log(error);
    process.exit();
  }

  if (response.statusCode !== 200) {
    console.log('Error:', response.statusCode);
    process.exit();
  }

  const data = JSON.parse(body);
  const result = {};
  let id = 0;

  data.forEach((user) => {
    id = user.userId;

    if (!(Object.prototype.hasOwnProperty.call(result, id))) {
      result[id] = 0;
    }

    if (user.completed) {
      result[id] += 1;
    }
  });
  console.log(result);
});
