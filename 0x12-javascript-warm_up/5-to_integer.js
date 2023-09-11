#!/usr/bin/node
const args = process.argv;
const len = args.length;
if (len < 3 || !parseInt(args[2])) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(args[2])}`);
}
