# Functions README

This repository contains a collection of JavaScript scripts that demonstrate the use of various functions for different tasks. Each script is designed to perform a specific function and is described below:

## 5-to_integer.js

This script checks if the first command-line argument can be converted to an integer and prints "My number: <number>" if successful. If the argument cannot be converted to an integer, it prints "Not a number."

Usage:
```
./5-to_integer.js
./5-to_integer.js 89
./5-to_integer.js "89"
./5-to_integer.js 89.89
./5-to_integer.js School
```

## 6-multi_languages_loop.js

This script prints three lines using a loop and an array of strings. Each line represents a programming language, and it uses only one `console.log` statement.

Usage:
```
./6-multi_languages_loop.js
```

## 7-multi_c.js

This script prints "C is fun" a specified number of times based on the first command-line argument. It handles cases where the argument is missing or not a positive integer.

Usage:
```
./7-multi_c.js 2
./7-multi_c.js 5
./7-multi_c.js
./7-multi_c.js -3
```

## 8-square.js

This script prints a square made of 'X' characters with a size specified by the first command-line argument. It handles cases where the argument is missing or not a positive integer.

Usage:
```
./8-square.js
./8-square.js School
./8-square.js 2
./8-square.js 6
./8-square.js -3
```

## 9-add.js

This script computes and prints the addition of two integers based on the first and second command-line arguments. It handles cases where one or both arguments are missing.

Usage:
```
./9-add.js
./9-add.js 1
./9-add.js 1 7
./9-add.js 13 89
```

## 10-factorial.js

This script computes and prints the factorial of an integer based on the first command-line argument. It handles cases where the argument is missing or not a valid integer.

Usage:
```
./10-factorial.js
./10-factorial.js 3
./10-factorial.js 89
./10-factorial.js 333
```

## 11-second_biggest.js

This script searches for the second biggest integer in a list of command-line arguments and prints it. It handles cases where no valid integers are provided or only one argument is provided.

Usage:
```
./11-second_biggest.js
./11-second_biggest.js 1
./11-second_biggest.js 4 2 5 3 0 -3
```

## 12-object.js

This script demonstrates how to update the value of a property in an object. It replaces the value '12' with '89' in the object and prints the object before and after the update.

Usage:
```
./12-object.js
```

## 13-add.js

This script defines a function named `add` that takes two integers and returns their sum. It exports the `add` function so that it can be used in other scripts. The `13-main.js` script imports and uses the `add` function.

Usage:
```
./13-main.js
```

## 101-call_me_moby.js

This script exports a function named `callMeMoby` that executes another function `x` times. The `101-main.js` script demonstrates the use of the `callMeMoby` function to print "C is fun" three times.

Usage:
```
./101-main.js
```

## 102-add_me_maybe.js

This script exports a function named `addMeMaybe` that increments a number and then calls another function with the incremented value. The `102-main.js` script demonstrates the use of the `addMeMaybe` function to increment a number and call a function.

Usage:
```
./102-main.js
```

## 103-object_fct.js

This script updates an object to include a function `incr` that increments an integer value. It then demonstrates the use of the `incr` function to increment the value multiple times.

Usage:
```
./103-object_fct.js
```

Feel free to explore and use these scripts for your own purposes.
```
