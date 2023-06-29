# Test-Driven Development (TDD) Python Scripts

This repository contains Python scripts that follow the principles of Test-Driven Development (TDD). Each script solves a specific problem and includes corresponding test cases to ensure the functionality and correctness of the code.

## Requirements

- Python Scripts
  - Allowed editors: vi, vim, emacs
  - All files should end with a new line
  - All files must be executable
  - The length of your files will be tested using the `wc` command
  - The first line of all files should be exactly `#!/usr/bin/python3`
  - Your code should adhere to the PEP 8 style guide (version 2.8.\*)
  - A `README.md` file, at the root of the project folder, is mandatory
- Python Test Cases
  - Allowed editors: vi, vim, emacs
  - All test files should be placed inside a folder named `tests`
  - All test files should be text files with the `.txt` extension
  - All your test files should end with a new line
  - All tests should be executed using the command: `python3 -m doctest ./tests/*`
  - All modules should have documentation (run `python3 -c 'print(__import__("my_module").__doc__)'`)
  - All functions should have documentation (run `python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
  - The documentation should provide a clear explanation of the purpose of the module, class, or method
  - Collaboration on test cases is strongly encouraged to cover all possible edge cases
  - The testing framework used is `doctest`

## Scripts and Test Cases

1. **Integers addition**
   - Filename: `0-add_integer.py`
   - Test File: `tests/0-add_integer.txt`
   - Function: `def add_integer(a, b=98)`
   - Description: This function adds two integers and returns the result. If the input is not an integer or float, a `TypeError` is raised.
   - Example:
     ```python
     add_integer(1, 2)  # Returns: 3
     add_integer(100, -2)  # Returns: 98
     add_integer(2)  # Returns: 100
     add_integer(100.3, -2)  # Returns: 98
     ```

2. **Divide a matrix**
   - Filename: `2-matrix_divided.py`
   - Test File: `tests/2-matrix_divided.txt`
   - Function: `def matrix_divided(matrix, div)`
   - Description: This function divides all elements of a matrix by a given number and returns a new matrix. If the input is not a matrix or the division factor is not a number, a `TypeError` is raised. If the division factor is zero, a `ZeroDivisionError` is raised.
   - Example:
     ```python
     matrix = [
        [1, 2, 3],
        [4, 5, 6]
     ]
     matrix_divided(matrix, 3)
     # Returns: [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
     ```

3. **Say my name**
   - Filename: `3-say_my_name.py`
   - Test File: `tests/3-say_my_name.txt`
   - Function: `def say_my_name(first_name, last_name="")`
   - Description: This function prints "My name is <first name> <last name>". If the

 inputs are not strings, a `TypeError` is raised.
   - Example:
     ```python
     say_my_name("John", "Doe")  # Prints: My name is John Doe
     say_my_name("Jane")  # Prints: My name is Jane
     ```

4. **Print square**
   - Filename: `4-print_square.py`
   - Test File: `tests/4-print_square.txt`
   - Function: `def print_square(size)`
   - Description: This function prints a square using the `#` character. The size of the square is determined by the input parameter. If the input is not an integer or less than 0, a `TypeError` or `ValueError` is raised, respectively.
   - Example:
     ```python
     print_square(5)
     # Prints:
     # #####
     # #####
     # #####
     # #####
     # #####

     print_square(2)
     # Prints:
     # ##
     # ##
     ```

5. **Text indentation**
   - Filename: `5-text_indentation.py`
   - Test File: `tests/5-text_indentation.txt`
   - Function: `def text_indentation(text)`
   - Description: This function prints a given text with two new lines after each occurrence of `.`, `?`, or `:`. If the input is not a string, a `TypeError` is raised.
   - Example:
     ```python
     text = "This is a sample text. It will be indented. Right? Yes!"
     text_indentation(text)
     # Prints:
     # This is a sample text.
     #
     # It will be indented.
     #
     # Right?
     #
     # Yes!
     ```

6. **Max integer - Unittest**
   - Filename: `6-max_integer_test.py`
   - Test File: `tests/6-max_integer_test.py`
   - Description: This script contains unit tests for the `max_integer` function. It uses the `unittest` module to perform the tests. The goal is to cover all possible edge cases.
   - Test Execution: `python3 -m unittest tests.6-max_integer_test`

## Contributing

Contributions to this repository are welcome. If you find any issues or want to add new features, feel free to submit a pull request. However, please ensure that your code follows the established guidelines and passes all the provided test cases.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
