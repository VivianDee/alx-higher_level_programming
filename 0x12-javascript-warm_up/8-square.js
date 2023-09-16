#!/usr/bin/node
let num = parseInt(process.argv[2]);
const width = num;
const myStr = 'X';
if (!num) {
  console.log('Missing size');
}
while (num > 0) {
  console.log(myStr.repeat(width));
  num--;
}
