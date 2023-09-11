#!/usr/bin/node
//  function that increments and calls a function.

let num = 0;
function addMeMaybe (x, theFunction) {
  num += x;
  theFunction(num);
}

module.exports = {
  addMeMaybe
};
