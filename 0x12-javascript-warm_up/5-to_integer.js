#!/usr/bin/node

// prints My number: <first argument converted in integer>

const arg = process.argv[2]; // Get the first command-line argument

const number = parseInt(arg, 10); // Attempt to parse the argument as an integer

if (!isNaN(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
