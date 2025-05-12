"""
Write a function to multiply two integers.
assert multiply_int(10,20)==200
"""
def multiply_int(a,b):
    return a*b

print(multiply_int(10,20))

"""
Write a function to multiply two floats.
assert multiply_float(10.0,20.0)==200.0
"""
def multiply_float(a,b):
    return a*b

print(multiply_float(10.0,20.0))

"""
Write a function to multiply two strings.
assert multiply_string("hello","world")=="helloworld"
"""
def multiply_string(a,b):
    return a+b

print(multiply_string("hello","world"))

"""
Write a function to multiply two lists.
assert multiply_list([1,2,3],[4,5,6])==[4,10,18]
"""
def multiply_list(a,b):
    return [a[i]*b[i] for i in range(len(a))]

print(multiply_list([1,2,3],[4,5,6]))

"""
Write a function to multiply two tuples.
assert multiply_tuple((1,2,3),(4,5,6))==[4,10,18]
"""
def multiply_tuple(a,b):
    return [a[i]*b[i] for i in range(len(a))]

print(multiply_tuple((1,2,3),(4,5,6)))

"""
Write a function to multiply two dictionaries.
assert multiply_dict({"a":1,"b":2},{"a":3,"b":4})=={"a":3,"b":8}
"""
def multiply_dict(a,b):
    return {a[i]:a[i]*b[i] for i in a}

print(multiply_dict({"a":1,"b":2},{"a":3,"b":4}))

"""
Write a function to multiply two sets.
assert multiply_set({1,2,3},{4,5,6})=={24}
"""
def multiply_set(a,b):
    return {a[i]*b[i] for i in a}

print(multiply_set({1,2,3},{4,5,6}))

"""
Write a function to multiply two frozensets.
assert multiply_frozenset({1,2,3},{4,5,6})=={24}
"""
def multiply_frozenset(a,b):
    return {a[i]*b[i] for i in a}

print(multiply_frozenset({1,2,3},{4,5,6}))

"""
Write a function to multiply two complex numbers.
assert multiply_complex(1+2j,3+4j)==-5+10j
"""
def multiply_complex(a,b):
    return a*b

print(multiply_complex(1+2j,3+4j))

"""
Write a function to multiply two numbers.
assert multiply_number(10,20)==200
"""
def multiply_number(a,b):
    return a*b

print(multiply_number(10,20))

"""
Write a function to multiply two booleans.
assert multiply_bool(True,False)==False
"""
def multiply_bool(a,b):
    return a*b

print(multiply_bool(True,False))

"""
Write a function to multiply two None.
assert multiply_none(None,None)==None
"""
def multiply_none(a,b):
    return a*b

print(multiply_none(None,None))

"""
Write a function to multiply two functions.
assert multiply_function(lambda x:x+1,lambda x:x+2)==lambda x:x+3
"""
def multiply_function(a,b):
    return a*b

print(multiply_function(lambda x:x+1,lambda x:x+2))

"""
Write a function to multiply two methods.
assert multiply_method(lambda x:x+1,lambda x:x+2)==lambda x:x+3
"""
def multiply_method(a