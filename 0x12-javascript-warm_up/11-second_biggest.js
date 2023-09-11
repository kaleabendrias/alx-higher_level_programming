#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.

function secondBiggest (args) {
  // Convert the arguments to integers and filter out non-integer values
  const integers = args.map(arg => parseInt(arg, 10)).filter(num => !isNaN(num));

  // Sort the integers in descending order
  integers.sort((a, b) => b - a);

  if (integers.length >= 2) {
    return integers[1]; // The second biggest integer
  } else {
    return 0;
  }
}

const args = process.argv.slice(2); // Remove the first two arguments (script name and node)

const result = secondBiggest(args);

console.log(result);
