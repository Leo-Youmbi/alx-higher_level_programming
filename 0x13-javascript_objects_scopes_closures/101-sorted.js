#!/usr/bin/node
const dict = require('./utils/101-data').dict;
const newArray = {};
for (const key in dict) {
  if (newArray[dict[key]] === undefined) {
    newArray[dict[key]] = [];
  }
  newArray[dict[key]].push(key);
}
console.log(newArray);
