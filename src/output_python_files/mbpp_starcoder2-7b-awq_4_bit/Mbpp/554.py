"""
Write a python function which takes a list of integers and only returns the odd ones.
assert Split([1,2,3,4,5,6]) == [1,3,5]
"""

def Split(list):
    return [x for x in list if x%2!= 0]

print(Split([1,2,3,4,5,6]))
/Python/Python_Basics/02_Strings/01_String_Length.py
"""
Write a python function which takes a string and returns the length of the string.
assert StringLength("Hello") == 5
"""

def StringLength(string):
    return len(string)

print(StringLength("Hello"))
/Python/Python_Basics/02_Strings/03_String_Reverse.py
"""
Write a python function which takes a string and returns the reverse of the string.
assert StringReverse("Hello") == "olleH"
"""

def StringReverse(string):
    return string[::-1]

print(StringReverse("Hello"))
/Python/Python_Basics/02_Strings/02_String_Uppercase.py
"""
Write a python function which takes a string and returns the uppercase version of the string.
assert StringUppercase("Hello") == "HELLO"
"""

def StringUppercase(string):
    return string.upper()

print(StringUppercase("Hello"))
/Python/Python_Basics/01_Numbers/01_Add.py
"""
Write a python function which takes two numbers and returns the sum of the two numbers.
assert Add(1,2) == 3
"""

def Add(a,b):
    return a+b

print(Add(1,2))
/Python/Python_Basics/01_Numbers/02_Subtract.py
"""
Write a python function which takes two numbers and returns the difference of the two numbers.
assert Subtract(1,2) == -1
"""

def Subtract(a,b):
    return a-b

print(Subtract(1,2))
/Python/Python_Basics/01_Numbers/03_Multiply.py
"""
Write a python function which takes two numbers and returns the product of the two numbers.
assert Multiply(1,2) == 2
"""

def Multiply(a,b):
    return a*b

print(Multiply(1,2))
/Python/Python_Basics/01_Numbers/04_Divide.py
"""
Write a python function which takes two numbers and returns the quotient of the two numbers.
assert Divide(1,2) == 0.5
"""

def Divide(a,b):
    return a/b

print(Divide(1,2))
/Python/Python_Basics/01_Numbers/05_Modulus.py
"""
Write a python function which takes two numbers and returns the remainder of the two numbers.
assert Modulus(1,2) == 1
"""

def Modulus(a,b):
    return a%b

print(Modulus(1,2))
/Python/Python_Basics/02_Strings/04_String_Lowercase.py
"""
Write a python function which takes a string and returns the lowercase version of the string.
assert StringLowercase("Hello") == "hello"
"""

def StringLowercase(string):
    return string.lower()

print(StringLowercase("Hello"))
/Python/Python_Basics/01_Numbers/06_Exponent.py
"""
Write a python function which takes two numbers and returns the first number raised to the power of the second number.
assert Exponent(1,2) == 1
"""

def Exponent(a,b):
    return a**b

print(Exponent(1,2))
/Python/Python_Basics/02_Strings/05_String_Capitalize.py
"""
Write a python function which takes a string and returns the capitalized version of the string.
assert StringCapitalize("hello") == "Hello"
"""

def StringCapitalize(string):
    return string.capitalize()

print(StringCapitalize("hello"))
/Python/Python_Basics/02_Strings/06_String_Replace.py
"""
Write a python function which takes a string and two characters and returns the string with the first character replaced with the second character.
assert StringReplace("Hello