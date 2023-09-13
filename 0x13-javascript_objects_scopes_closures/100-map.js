#!/usr/bin/node
const myList = require('./100-data').list;
const myArray = myList.map( (element, index) => {
    return element * index;
});
console.log(myList);
console.log(myArray);
