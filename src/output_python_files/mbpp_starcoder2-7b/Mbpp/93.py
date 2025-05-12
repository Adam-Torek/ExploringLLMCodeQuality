"""
Write a function to calculate the value of 'a' to the power 'b'.
assert power(3,4) == 81
"""

def power(a,b):
    return a**b

print(power(3,4))
/python/python_basics/02_variables.py
"""
Variables
"""

# Variables are containers for storing data values.

# Variables are created when you assign a value to it.

# Variables do not need to be declared with any particular type and can even change type after they have been set.

# Python is a dynamically typed language, so you do not need to specify the type of a variable.

# This example assigns an integer value to a variable named x:

x = 5
print(x)

# This example assigns a string value to a variable named y:

y = "John"
print(y)

# This example assigns a floating point value to a variable named z:

z = 20.5
print(z)

# This example assigns a boolean value to a variable named a:

a = True
print(a)

# This example assigns a complex number value to a variable named b:

b = 3 + 5j
print(b)

# This example assigns a list value to a variable named c:

c = [1, 2, 3]
print(c)

# This example assigns a tuple value to a variable named d:

d = (1, 2, 3)
print(d)

# This example assigns a set value to a variable named e:

e = {1, 2, 3}
print(e)

# This example assigns a frozen set value to a variable named f:

f = frozenset({1, 2, 3})
print(f)

# This example assigns a dictionary value to a variable named g:

g = {"name": "John", "age": 36}
print(g)

# This example assigns a range value to a variable named h:

h = range(6)
print(h)

# This example assigns a bytes value to a variable named i:

i = b"Hello"
print(i)

# This example assigns a byte array value to a variable named j:

j = bytearray(5)
print(j)

# This example assigns a memoryview value to a variable named k:

k = memoryview(bytes(5))
print(k)

# This example assigns a None value to a variable named l:

l = None
print(l)

# This example assigns a class value to a variable named m:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

m = Person("John", 36)
print(m)

# This example assigns a function value to a variable named n:

def my_function():
    print("Hello from a function")

n = my_function
print(n)

# This example assigns a lambda value to a variable named o:

o = lambda a, b: a + b
print(o)

# This example assigns a generator value to a variable named p:

p = (x * 2 for x in range(10))
print(p)

# This example assigns a module value to a variable named q:

q = __name__
print(q)

# This example assigns a built-in function value to a variable named r:

r = abs
print(r)

# This example assigns a built-in method value to a variable named s:

s = dir
print(s)

# This example assigns a built-in class value to a variable named t:

t = dict
print(t)

# This example assigns a built-in type value to a variable named u:

u = type
print(u)

# This example assigns a built-in property value to a variable named v:

v = property
print(v)

# This example assigns a built-in class method value to a variable named w:

w = object.__init__
print(w)

# This example assigns a built-in class attribute value to a variable named x:

x = object.__doc__
print(x)