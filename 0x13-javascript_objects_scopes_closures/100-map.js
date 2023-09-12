#!/usr/bin/node

const data = require('./100-data.js');

const originalList = data.list;

console.log(originalList.list);
console.log(originalList.list.map((x, idx) => x * idx));
