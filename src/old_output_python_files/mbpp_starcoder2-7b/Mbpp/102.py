"""
Write a function to convert a snake case string to camel case string.
assert snake_to_camel('python_program')=='PythonProgram'
"""

def snake_to_camel(s):
    return s.title().replace('_','')

print(snake_to_camel('python_program'))
<file_sep>/python_basics/02_data_types/01_numbers.py
"""
Numbers
"""

# Integer
print(10)
print(type(10))

# Float
print(10.5)
print(type(10.5))

# Complex
print(10+5j)
print(type(10+5j))

# Boolean
print(True)
print(type(True))

# None
print(None)
print(type(None))

# Type conversion
print(int(10.5))
print(float(10))
print(complex(10))
print(bool(10))
print(bool(0))
print(bool(None))
print(bool(''))
print(bool(' '))
print(bool('a'))
print(bool([]))
print(bool([1,2,3]))
print(bool({}))
print(bool({'a':1}))

# Arithmetic operators
print(10+5)
print(10-5)
print(10*5)
print(10/5)
print(10//5)
print(10%5)
print(10**5)

# Assignment operators
a = 10
a += 5
print(a)
a -= 5
print(a)
a *= 5
print(a)
a /= 5
print(a)
a //= 5
print(a)
a %= 5
print(a)
a **= 5
print(a)

# Comparison operators
print(10==10)
print(10!=10)
print(10>10)
print(10<10)
print(10>=10)
print(10<=10)

# Logical operators
print(True and True)
print(True and False)
print(False and True)
print(False and False)
print(True or True)
print(True or False)
print(False or True)
print(False or False)
print(not True)
print(not False)

# Bitwise operators
print(10 & 5)
print(10 | 5)
print(10 ^ 5)
print(~10)
print(10 << 2)
print(10 >> 2)

# Identity operators
print(10 is 10)
print(10 is not 10)

# Membership operators
print(10 in [10,20,30])
print(10 not in [10,20,30])

# Operator precedence
print(10+5*2)
print((10+5)*2)
print(10+5/2)
print(10+5//2)
print(10+5%2)
print(10+5**2)
print(10+5&2)
print(10+5|2)
print(10+5^2)
print(10+5<<2)
print(10+5>>2)
print(10+5==2)
print(10+5!=2)
print(10+5>2)
print(10+5<2)
print(10+5>=2)
print(10+5<=2)
print(10+5 and 2)
print(10+5 or 2)
print(10+5 is 2)
print(10+5 is not 2)
print(10+5 in 2)
print(10+5 not in 2)
<file_sep>/python_basics/03_control_flow/02_loops.py
"""
Loops
"""

# For loop
for i in range(10):
    print(i)

for i in range(10):
    print(i, end=' ')

for i in range(10):
    print(i, end=' ')
else: