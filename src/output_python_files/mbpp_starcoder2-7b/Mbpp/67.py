"""
Write a function to find the number of ways to partition a set of Bell numbers.
assert bell_number(2)==2
"""

def bell_number(n):
    """
    >>> bell_number(2)
    2
    """
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return bell_number(n-1) + sum(bell_number(k) for k in range(n-1))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/README.md
# CS61A

This is a repository for my work in CS61A, a course on computer science and programming in Python.

## Course Description

This course is an introduction to the Python programming language. It covers the basics of programming, including variables, expressions, functions, conditionals, iteration, and lists. It also covers the basics of object-oriented programming, including classes, methods, and inheritance.

## Course Outcomes

By the end of the course, students will be able to:

- Write programs that use variables, expressions, and functions.
- Write programs that use conditionals and iteration.
- Write programs that use lists and list operations.
- Write programs that use classes and objects.
- Write programs that use inheritance.
- Write programs that use recursion.
- Write programs that use higher-order functions.
- Write programs that use the Python standard library.
- Write programs that use the Python interpreter.
- Write programs that use the Python debugger.
- Write programs that use the Python unit testing framework.
- Write programs that use the Python documentation system.
- Write programs that use the Python package manager.
- Write programs that use the Python virtual environment.
- Write programs that use the Python version control system.
- Write programs that use the Python build system.
- Write programs that use the Python packaging system.
- Write programs that use the Python deployment system.
- Write programs that use the Python testing system.
- Write programs that use the Python continuous integration system.
- Write programs that use the Python continuous deployment system.
- Write programs that use the Python continuous testing system.
- Write programs that use the Python continuous monitoring system.
- Write programs that use the Python continuous improvement system.
- Write programs that use the Python continuous learning system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use the Python continuous refactoring system.
- Write programs that use