def derivative(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
     Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """

def integrate(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
     Return integral of this polynomial in the same form.
    >>> integrate([3, 1, 2, 4, 5])
    [0, 3, 1, 4, 5]
    >>> integrate([1, 2, 3])
    [0, 1, 3]
    """

def roots(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
     Return roots of this polynomial in the same form.
    >>> roots([3, 1, 2, 4, 5])
    [-1.0, -0.5]
    >>> roots([1, 2, 3])
    [-1.5]
    """

def plot(xs: list):
    """ xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 +....
     Plot this polynomial.
    >>> plot([3, 1, 2, 4, 5])
    >>> plot([1, 2, 3])
    """

def main():
    """ Main function.
    """

if __name__ == '__main__':
    main()
/README.md
# Polynomial

This is a simple polynomial class.

## Installation

```bash
pip install -e.
```

## Usage

```python
from polynomial import Polynomial

p = Polynomial([1, 2, 3])
print(p)
print(p.derivative())
print(p.integrate())
print(p.roots())
p.plot()
```

## License

[MIT](https://choosealicense.com/licenses/mit/)