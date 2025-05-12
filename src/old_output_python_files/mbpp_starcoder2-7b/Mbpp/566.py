"""
Write a function to get the sum of the digits of a non-negative integer.
assert sum_digits(345)==12
"""
def sum_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

print(sum_digits(345))
<file_sep>/python/python_basics/02_variables.py
"""
Variables
"""

# Variables are used to store information to be referenced and manipulated in a computer program.

# Variables are created when you assign a value to it.

# Python variables do not need explicit declaration to reserve memory space.
# The declaration happens automatically when you assign a value to a variable.

# The equal sign (=) is used to assign values to variables.

# Python uses the word "variable" to describe a value that can change over the course of a program.

# Python has a number of different data types available for its variables.

# Python has five standard data types −
# Numbers, String, List, Tuple, Dictionary

# Python Numbers
# Number data types store numeric values. Number objects are created when you assign a value to them.

# There are three different numerical types −
# int − for storing integer numbers.
# float − for storing floating point numbers.
# complex − for storing complex numbers.

# Python Strings
# Strings are sequences of Unicode characters.
# We can use single quotes or double quotes to represent strings.
# Multi-line strings can be denoted using triple quotes, ''' or """.

# Python Lists
# Lists are the most versatile of Python's compound data types.
# A list contains items separated by commas and enclosed within square brackets ([]).
# To some extent, lists are similar to arrays in C.
# One difference between them is that all the items belonging to a list can be of different data type.

# Python Tuples
# Tuples are similar to lists but only big difference is the elements inside a list can be changed but in tuple it cannot be changed.
# Think of tuples as something which has to be True for a particular something and cannot be True for no other values.
# For example − A student cannot change his/her roll number.
# Tuples are enclosed within parentheses (()).

# Python Dictionary
# Dictionary is an unordered collection of key-value pairs.
# In Python, dictionaries are defined within braces {} with each item being a pair in the form key:value.
# Key and value can be of any type.

# Python Booleans
# Boolean represents the truth values False and True.

# Python Operators
# Operators are the constructs which can manipulate the value of operands.
# Consider the expression 4 + 5 = 9. Here, 4 and 5 are called operands and + is called operator.

# Python Operands
# Operands are the values on which operation is applied.

# Python Operators
# Operators are special symbols in Python that carry out arithmetic or logical computation.
# The value that the operator operates on is called the operand.

# Python Operands
# Operands are the values on which operation is applied.

# Python Expressions
# Expressions are combinations of operands and operators.

# Python Statements
# Statements are the instructions that a Python interpreter can execute.
# They define the program logic.

# Python Comments
# Comments are lines that exist in computer programs that are ignored by compilers and interpreters.
# In Python, comments are given using hash (#) symbol.
# Hash (#) symbol is used to start a comment.
# All characters after the # and up to the end of the physical line are part of the comment and the Python interpreter ignores them.

# Python Indentation
# Most of the programming languages like C, C++, Java use braces { } to define a block of code.
# Python uses indentation.

# Python Indentation
# Most of the programming languages like C, C++, Java use braces { } to define a block of code.
# Python uses indentation.

# Python Identifiers
# An identifier is a name given to entities like class, functions, variables, etc.
# It helps to differentiate one entity from another.

# Rules for Writing Identifiers
# 1. Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore (_).
# 2. An identifier cannot start with a digit. 1variable is invalid, but variable1 is