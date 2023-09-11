#!/usr/bin/node
//  function that increments and calls a function.

function addMeMaybe (number, theFunction) {
  number++; // Increment the number
  theFunction(number); // Call the provided function with the incremented number
}

module.exports = {
  addMeMaybe
};
