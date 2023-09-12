#!/usr/bin/node

const data = require('./100-data.js');

const originalList = data.list;

const newList = originalList.map(function (value, index) {
  return value * index;
});
