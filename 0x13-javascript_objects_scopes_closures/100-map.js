#!/usr/bin/node
const list = require('./utils/100-data.js').list;
console.log(list);
console.log(list.map((i, ndx) => ndx * i));
