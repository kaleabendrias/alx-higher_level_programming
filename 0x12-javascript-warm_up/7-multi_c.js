#!/usr/bin/node
// script that prints x times “C is fun”

const arg = process.argv;

const x = parseInt(arg[2], 10);

if (!isNaN(x)) {
  for (let i = 0; i < args[2]; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
