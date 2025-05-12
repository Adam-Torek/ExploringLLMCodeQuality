"""
Write a function to sort the given list.
assert heap_sort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

def heap_sort(lst):
    """
    Sort the given list.
    """
    # TODO: Implement me
    pass
/0x00-lockboxes/README.md
# 0x00. Lockboxes

## Background Context

In this project, you will learn how to handle multiple locks at the same time.

## Resources

### Read or watch:

- [Lock](https://intranet.hbtn.io/rltoken/)
- [LockManager](https://intranet.hbtn.io/rltoken/)
- [with](https://intranet.hbtn.io/rltoken/)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- Why Python programmers have always been afraid of locks.
- How to manage multiple locks in a single thread.
- How to manage multiple locks in a multi-threaded environment.

## Requirements

### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `PEP 8` style (version 1.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should be documented: `python3 -c 'print(__import__("my_module").__doc__)'`
- All your classes should be documented: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
- All your functions (inside and outside a class) should be documented: `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Tasks

### 0. Lockboxes

Write a class `LockBox` that manages locks.

- Public instance attributes:
    - `id`
    - `size`
- Class constructor:
    - `def __init__(self, id=None, size=0):`
        - `id`: `str`
        - `size`: `int`
        - If `id` is `None`, generate a random `id`
        - If `size` is less than `1`, raise a `ValueError` exception with the message `size must be >= 1`
- Public instance methods:
    - `def lock(self):`
        - Lock the box
    - `def unlock(self):`
        - Unlock the box
    - `def __str__(self):`
        - Returns the `str` representation of the `LockBox` instance

### 1. Lockboxes #0

Write a class `LockBox` that manages locks.

- Public instance attributes:
    - `id`
    - `size`
- Class constructor:
    - `def __init__(self, id=None, size=0):`
        - `id`: `str`
        - `size`: `int`
        - If `id` is `None`, generate a random `id`
        - If `size` is less than `1`, raise a `ValueError` exception with the message `size must be >= 1`
- Public instance methods:
    - `def lock(self):`
        - Lock the box
    - `def unlock(self):`
        - Unlock the box
    - `def __str__(self):`
        - Returns the `str` representation of the `LockBox` instance

### 2. Lockboxes #1

Write a class `LockBox` that manages locks.

- Public instance attributes:
    - `id`