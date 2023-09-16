#!/usr/bin/node
let num = parseInt(process.argv[2]);
if (!num) {
  console.log('Missing number of occurrences');
}
while (num > 0) {
  console.log('C is fun');
  num--;
}
