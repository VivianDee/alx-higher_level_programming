#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
fs.readFile(file, 'utf8', (error, body) => {
  if (error) throw error;
  console.log(body);
});
