# Square Class

This repository contains the implementation of the `Square` class, which defines a square and provides various functionalities related to squares.

## Requirements

- Python version: 3.8.5
- Code style: PEP 8 (pycodestyle version 2.8.*)

## Usage

1. Clone the repository:
   ```
   git clone https://github.com/username/alx-higher_level_programming.git
   ```

2. Import the `Square` class into your Python script:
   ```python
   from square import Square
   ```

3. Create an instance of the `Square` class:
   ```python
   my_square = Square()
   ```

4. Access and modify the attributes of the square object as needed:
   ```python
   my_square.size = 5
   area = my_square.area()
   my_square.my_print()
   ```

## Class Documentation

### `Square` class

#### Attributes

- `size`: Private instance attribute representing the size of the square.

#### Methods

- `__init__(self, size=0)`: Initializes a square object with an optional size. Size must be an integer, and if not provided, it defaults to 0.

- `area(self) -> int`: Computes and returns the area of the square.

- `my_print(self) -> None`: Prints the square using the '#' character. If the size is 0, it prints an empty line.

- `size` (property): Getter method to retrieve the size of the square.

- `size` (setter): Setter method to set the size of the square. It validates that the size is an integer and >= 0.

- `position` (property): Getter method to retrieve the position of the square.

- `position` (setter): Setter method to set the position of the square. It validates that the position is a tuple of 2 positive integers.

## Files

- `square.py`: Contains the implementation of the `Square` class.
- `main.py`: Examples demonstrating the usage of the `Square` class.

## Testing

To test the functionality of the `Square` class, run the `main.py` script:
```
python3 main.py
```

## Author

Created by Kaleab Endrias - https://github.com/kaleabendrias

Feel free to provide any feedback or suggestions!
