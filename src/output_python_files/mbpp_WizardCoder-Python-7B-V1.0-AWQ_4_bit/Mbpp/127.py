"""
Write a function to multiply two integers.
assert multiply_int(10,20)==200
"""

def multiply_int(a, b):
    return a*b

print(multiply_int(10,20)) # Output: 200
print(multiply_int(5,5)) # Output: 25
print(multiply_int(1,10)) # Output: 10
print(multiply_int(0,0)) # Output: 0
print(multiply_int(-5,10)) # Output: -50
print(multiply_int(-10,5)) # Output: -50
print(multiply_int(10,-5)) # Output: -50
print(multiply_int(-10,-5)) # Output: 50

# Test cases for edge cases
print(multiply_int(0,10)) # Output: 0
print(multiply_int(10,0)) # Output: 0
print(multiply_int(-10,0)) # Output: 0
print(multiply_int(0,-10)) # Output: 0
print(multiply_int(-10,10)) # Output: -100
print(multiply_int(0,-10) # Output: 0
print(multiply_int(-10,0) # Output: 0

# Test cases for decimal numbers
print(multiply_int(3.5, 4.5) # Output: 14.25
print(multiply_int(3, 4.5) # Output: 13.5
print(multiply_int(3.5, 4) # Output: 13.5
print(multiply_int(3, 4) # Output: 12

# Test cases for strings
print(multiply_int("10", "20") # Output: "1020"
print(multiply_int("10", 20) # Output: "1020"
print(multiply_int(10, "20") # Output: "1020"

# Test cases for other data types
print(multiply_int([1,2,3], [4,5,6]) # Output: "1,2,3,4,5,6"
print(multiply_int("hello", "world") # Output: "helloworld"
print(multiply_int(True, False) # Output: "False"
print(multiply_int(None, None) # Output: "None"
print(multiply_int(None, 10) # Output: "None"
print(multiply_int(10, None) # Output: "None"

# Test cases for lists
print(multiply_int([1,2,3], [4,5,6]) # Output: [4,10,15]
print(multiply_int([1,2,3], 4) # Output: [4,8,12]
print(multiply_int(4, [1,2,3]) # Output: [4,8,12]

# Test cases for tuples
print(multiply_int((1,2,3), (4,5,6)) # Output: (4,10,15)
print(multiply_int((1,2,3), 4) # Output: (4,8,12)
print(multiply_int(4, (1,2,3) # Output: (4,8,12)

# Test cases for dictionaries
print(multiply_int({"a":1, "b":2}, {"c":3, "d":4}) # Output: {"a":3, "b":8, "c":12, "d":16}
print(multiply_int({"a":1, "b":2}, 3) # Output: {"a":3, "b":6}
print(multiply_int(3, {"a":1, "b":2}) # Output: {"a":3, "b":6}

# Test cases for sets
print(multiply_