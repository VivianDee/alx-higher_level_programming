#!/usr/bin/node
const args = process.argv;
const len = args.length;
let high = 0;
let low = 0;
for (let i = 2; i < len; i++) {
	if (parseInt(args[i]) > high) {
		low = high;
		high = parseInt(args[i]);
	}
}
console.log(low);
