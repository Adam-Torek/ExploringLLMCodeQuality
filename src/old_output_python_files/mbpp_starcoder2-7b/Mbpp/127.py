"""
Write a function to multiply two integers.
assert multiply_int(10,20)==200
"""

def multiply_int(a,b):
    return a*b

print(multiply_int(10,20))

"""
Write a function to multiply two floats.
assert multiply_float(10.5,20.5)==212.75
"""

def multiply_float(a,b):
    return a*b

print(multiply_float(10.5,20.5))

"""
Write a function to multiply two strings.
assert multiply_string("abc","def")==abcdef
"""

def multiply_string(a,b):
    return a*b

print(multiply_string("abc","def"))

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
    return {k:a[k]*b[k] for k in a}

print(multiply_dict({"a":1,"b":2},{"a":3,"b":4}))

"""
Write a function to multiply two sets.
assert multiply_set({1,2,3},{4,5,6})=={4,10,18}
"""

def multiply_set(a,b):
    return {a[i]*b[i] for i in range(len(a))}

print(multiply_set({1,2,3},{4,5,6}))

"""
Write a function to multiply two frozensets.
assert multiply_frozenset({1,2,3},{4,5,6})=={4,10,18}
"""

def multiply_frozenset(a,b):
    return {a[i]*b[i] for i in range(len(a))}

print(multiply_frozenset({1,2,3},{4,5,6}))

"""
Write a function to multiply two complex numbers.
assert multiply_complex(1+2j,3+4j)==-5+10j
"""

def multiply_complex(a,b):
    return a*b

print(multiply_complex(1+2j,3+4j))

"""
Write a function to multiply two decimals.
assert multiply_decimal(Decimal(10.5),Decimal(20.5))==Decimal(212.75)
"""

def multiply_decimal(a,b):
    return a*b

print(multiply_decimal(Decimal(10.5),Decimal(20.5)))

"""
Write a function to multiply two fractions.
assert multiply_fraction(Fraction(10,20),Fraction(20,40))==Fraction(1,1)
"""

def multiply_fraction(a,b):
    return a*b

print(multiply_fraction(Fraction(10,20),Fraction(20,40)))

"""
Write a function to multiply two dates.
assert multiply_date(date(2019,1,1),date(2019,1,1))==date(2019,1,1)
"""

def multiply_date(a,b):
    return a*b

print(multiply_date(date(2019,1,1),date(2019,1,1)))

"""
Write a function to multiply two times.
assert multiply_time(time(10,20,30),time(1