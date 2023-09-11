#!/usr/bin/node
const args = process.argv;
const len = args.length;
if (len < 3) {
  console.log('No argument');
} else {
  console.log('Arguments found');
}
