"""
Write a python function to find the sum of non-repeated elements in a given list.
assert find_sum([1,2,3,1,1,4,5,6]) == 21
"""

def find_sum(lst):
    sum = 0
    for i in lst:
        if lst.count(i) == 1:
            sum += i
    return sum

print(find_sum([1,2,3,1,1,4,5,6]))
/python/python_basics/03_variables.py
"""
Variables
"""

# Variables are used to store data.
# Variables are declared using the equal sign (=)

# Example

x = 5
y = "John"
print(x)
print(y)

# Variables do not need to be declared with any particular type and can even change type after they have been set.

x = 4 # x is of type int
x = "Sally" # x is now of type str
print(x)

# Variable names are case-sensitive.

a = 4
A = "Sally"
print(a)
print(A)

# Variable names can be short but descriptive, for example:

myvar = 5
my_var = 5
_my_var = 5
myVar = 5
MYVAR = 5
myvar2 = 5

# Variable names cannot start with a number.

# 2myvar = 5

# Variable names cannot contain spaces.

# my var = 5

# Variable names are case-sensitive.

myvar = 5
MYVAR = 10

print(myvar)
print(MYVAR)

# Variable names cannot be any of the following words:

# and, as, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, while, with, yield

# Variable names can contain alphanumeric characters and underscores (a-z, A-Z, 0-9, _).

my_var = 5
my_var2 = "John"
my_var3 = "John"

# Variable names cannot contain special characters.

# my-var = 5

# Variable names cannot contain spaces.

# my var = 5

# Variable names cannot start with a number.

# 2myvar = 5

# Variable names are case-sensitive.

myvar = 4
MYVAR = 10

print(myvar)
print(MYVAR)

# Variable names cannot be any of the following words:

# and, as, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, while, with, yield

# Variable names can contain alphanumeric characters and underscores (a-z, A-Z, 0-9, _).

my_var = 5
my_var2 = "John"
my_var3 = "John"

# Variable names cannot contain special characters.

# my-var = 5

# Variable names cannot contain spaces.

# my var = 5

# Variable names cannot start with a number.

# 2myvar = 5

# Variable names are case-sensitive.

myvar = 4
MYVAR = 10

print(myvar)
print(MYVAR)

# Variable names cannot be any of the following words:

# and, as, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, while, with, yield

# Variable names can contain alphanumeric characters and underscores (a-z, A-