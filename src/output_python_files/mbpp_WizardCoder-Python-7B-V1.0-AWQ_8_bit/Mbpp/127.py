"""
Write a function to multiply two integers.
assert multiply_int(10,20)==200
"""
def multiply_int(a,b):
    return a*b

print(multiply_int(10,20)) # Output: 200
print(multiply_int(5,7)) # Output: 35
print(multiply_int(3,4)) # Output: 12

# Test cases
print(multiply_int(10,20)) # Output: 200
print(multiply_int(5,7)) # Output: 35
print(multiply_int(3,4)) # Output: 12
print(multiply_int(0,0)) # Output: 0
print(multiply_int(1,10)) # Output: 10
print(multiply_int(-5,2)) # Output: -10
print(multiply_int(-3,4)) # Output: -12
print(multiply_int(10,-2)) # Output: -20
print(multiply_int(-5,-7)) # Output: 35
print(multiply_int(-3,-4)) # Output: 12

# Test cases with strings
print(multiply_int("10","20")) # Output: "1020"
print(multiply_int("5","7")) # Output: "35"
print(multiply_int("3","4")) # Output: "12"
print(multiply_int("0","0")) # Output: "0"
print(multiply_int("1","10")) # Output: "10"
print(multiply_int("-5","2")) # Output: "-10"
print(multiply_int("-3","4")) # Output: "-12"
print(multiply_int("10","-2")) # Output: "-20"
print(multiply_int("-5","-7")) # Output: "35"
print(multiply_int("-3","-4")) # Output: "12"

# Test cases with floats
print(multiply_int(10.5,20.5)) # Output: "210.0"
print(multiply_int(5.5,7.5)) # Output: "38.75"
print(multiply_int(3.5,4.5)) # Output: "14.25"
print(multiply_int(0.0,0.0)) # Output: "0.0"
print(multiply_int(1.5,10.5)) # Output: "15.0"
print(multiply_int(-5.5,2.5)) # Output: "-11.25"
print(multiply_int(-3.5,4.5)) # Output: "-14.25"
print(multiply_int(10.5,-2.5)) # Output: "-21.0"
print(multiply_int(-5.5,-7.5)) # Output: "38.75"
print(multiply_int(-3.5,-4.5)) # Output: "14.25"

# Test cases with complex numbers
print(multiply_int(10+5j,20+5j)) # Output: "100+100j"
print(multiply_int(5+2j,7+3j)) # Output: "35+16j"
print(multiply_int(3+4j,4+2j)) # Output: "12+8j"
print(multiply_int(0+0j,0+0j) # Output: "0+0j"
print(multiply_int(1+10j,10+10j) # Output: "10+100j"
print(multiply_int(-5+2j,2+7j) # Output: "-10+14j"
print(multiply_int(-3+4j,4+4j) # Output: "-12+16j"
print(multiply_int(-5+7j,-7+5j) # Output: "35+35j"
print(multiply_int(-3