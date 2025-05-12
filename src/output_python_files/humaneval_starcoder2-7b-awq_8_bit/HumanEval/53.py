def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """

def sub(x: int, y: int):
    """Subtract two numbers x and y
    >>> sub(2, 3)
    -1
    >>> sub(5, 7)
    -2
    """

def mul(x: int, y: int):
    """Multiply two numbers x and y
    >>> mul(2, 3)
    6
    >>> mul(5, 7)
    35
    """

def div(x: int, y: int):
    """Divide two numbers x and y
    >>> div(2, 3)
    0
    >>> div(5, 7)
    0
    """

def main():
    """Main function
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()
/README.md
# Python-Unit-Testing

This repository contains the code for the unit testing of a simple calculator.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them

```
Python 3.6
```

### Installing

A step by step series of examples that tell you how to get a development env running

```
git clone https://github.com/siddharth-kumar-1997/Python-Unit-Testing.git
```

## Running the tests

```
python3 test_calculator.py
```

## Authors

* **** - *Initial work* - [siddharth-kumar-1997](https://github.com/siddharth-kumar-1997)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details