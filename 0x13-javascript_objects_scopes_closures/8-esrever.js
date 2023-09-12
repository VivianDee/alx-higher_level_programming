#!/usr/bin/node
exports.esrever = function (list) {
  const myList = [];
  let idx = 0;
  let len = list.length;

  while (idx < list.length) {
    myList[idx] = list[len - 1];
    len--;
    idx++;
  }

  return myList;
};
