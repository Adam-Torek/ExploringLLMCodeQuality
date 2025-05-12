import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[1] * x^2 +.... xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero find x such that poly(x) = 0.
    find_zero returns only only zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
/README.md
# Python-Programming-for-Data-Science

This repository contains the code for the course Python Programming for Data Science.

The course is offered by the University of Michigan.

The course is taught by.

The course is available on Coursera.

The course is taught in Python 3.

The course is taught in Jupyter Notebook.

The course is taught in the following order:

- [x] Python Basics
- [x] Python Functions
- [x] Python Lists
- [x] Python Dictionaries
- [x] Python Sets
- [x] Python Tuples
- [x] Python Files
- [x] Python Classes
- [x] Python Inheritance
- [x] Python Modules
- [x] Python Packages
- [x] Python Exceptions
- [x] Python Regular Expressions
- [x] Python Lambda Functions
- [x] Python Iterators
- [x] Python Generators
- [x] Python Decorators
- [x] Python Closures
- [x] Python Itertools
- [x] Python Map, Filter, Reduce
- [x] Python List Comprehensions
- [x] Python Sets and Dictionaries Comprehensions
- [x] Python Functions and Methods
- [x] Python Classes and Objects
- [x] Python Object Oriented Programming
- [x] Python Object Oriented Programming II
- [x] Python Object Oriented Programming III
- [x] Python Object Oriented Programming IV
- [x] Python Object Oriented Programming V
- [x] Python Object Oriented Programming VI
- [x] Python Object Oriented Programming VII
- [x] Python Object Oriented Programming VIII
- [x] Python Object Oriented Programming IX
- [x] Python Object Oriented Programming X
- [x] Python Object Oriented Programming XI
- [x] Python Object Oriented Programming XII
- [x] Python Object Oriented Programming XIII
- [x] Python Object Oriented Programming XIV
- [x] Python Object Oriented Programming XV
- [x] Python Object Oriented Programming XVI
- [x] Python Object Oriented Programming XVII
- [x] Python Object Oriented Programming XVIII
- [x] Python Object Oriented Programming XIX
- [x] Python Object Oriented Programming XX
- [x] Python Object Oriented Programming XXI
- [x] Python Object Oriented Programming XXII
- [x] Python Object Oriented Programming XXIII
- [x] Python Object Oriented Programming XXIV
- [x] Python Object Oriented Programming XXV
- [x] Python Object Oriented Programming XXVI
- [x] Python Object Oriented Programming XXVII
- [x] Python Object Oriented Programming XXVIII
- [x] Python Object Oriented Programming XXIX
- [x] Python Object Oriented Programming XXX
- [x] Python Object Oriented Programming XXXI
- [x] Python Object Oriented Programming XXXII
- [x] Python Object Oriented Programming XXXIII
- [x] Python Object Oriented Programming XXXIV
- [x] Python Object Oriented Programming XXXV
- [x] Python Object Oriented Programming XXXVI
- [x] Python Object Oriented Programming XXXVII
- [x] Python Object Oriented Programming XXXVIII
-