#!/usr/bin/node
const dict = require('./101-data').dict
const keys = Object.keys(dict);
const values = Object.values(dict);
let newDict = {}
let len = keys.length - 1;
while (len > -1) {
    newDict[values[len]] = [];
    len--;
}
len = values.length - 1;
while (len > -1) {
    newDict[values[len]].push(keys[len])
    len--;
}
console.log(newDict);
