def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """

def subtract(x: int, y: int):
    """Subtract two numbers x and y
    >>> subtract(2, 3)
    -1
    >>> subtract(5, 7)
    -2
    """

def multiply(x: int, y: int):
    """Multiply two numbers x and y
    >>> multiply(2, 3)
    6
    >>> multiply(5, 7)
    35
    """

def divide(x: int, y: int):
    """Divide two numbers x and y
    >>> divide(2, 3)
    0
    >>> divide(5, 7)
    0
    """

def main():
    """Main function
    """
    pass

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/README.md
# Python-Unit-Testing

This repository contains the code for the Python Unit Testing tutorial.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need to have Python 3.6 or higher installed on your machine.

### Installing

Clone the repository to your local machine.

```
git clone https://github.com/james-w-moore/Python-Unit-Testing.git
```

## Running the tests

To run the tests, navigate to the root directory of the project and run the following command:

```
python -m unittest discover -s tests -p "*_test.py"
```

## Built With

* [Python](https://www.python.org/) - The programming language used
* [PyCharm](https://www.jetbrains.com/pycharm/) - The IDE used

## Authors

* **** - *Initial work* - [james-w-moore](https://github.com/james-w-moore)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details