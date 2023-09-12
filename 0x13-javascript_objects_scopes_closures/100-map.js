#!/usr/bin/node

const data = require('./100-data.js');

const originalList = data.list;

console.log(originalList);
console.log(originalList.map((x, idx) => x * idx));
