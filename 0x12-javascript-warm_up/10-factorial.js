#!/usr/bin/node
// a script that computes and prints a factorial

function factorial(n) {
    if (isNaN(n) || n < 0) {
      return 1; // Factorial of NaN or negative number is 1
    }
  
    if (n === 0 || n === 1) {
      return 1; // Factorial of 0 or 1 is 1
    } else {
      return n * factorial(n - 1);
    }
  }
  
  const arg = process.argv[2];
  const num = parseInt(arg, 10);
  
  const result = factorial(num);
  
  console.log(result);
  