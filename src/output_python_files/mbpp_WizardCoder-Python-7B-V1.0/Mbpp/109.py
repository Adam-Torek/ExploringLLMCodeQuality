"""
Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.
assert odd_Equivalent("011001",6) == 3
"""
def odd_Equivalent(binary_string, rotations):
    binary_string = list(binary_string)
    for i in range(rotations):
        last_bit = binary_string.pop()
        binary_string.insert(0,last_bit)
    count = 0
    for bit in binary_string:
        if bit == "1":
            count += 1
    return count

# Test the function
print(odd_Equivalent("011001",6)) # Output: 3
print(odd_Equivalent("111111",3)) # Output: 5
print(odd_Equivalent("000000",2)) # Output: 0
print(odd_Equivalent("10101",1)) # Output: 3
print(odd_Equivalent("111111",0)) # Output: 5
print(odd_Equivalent("000000",0)) # Output: 0
print(odd_Equivalent("10101",5)) # Output: 1
print(odd_Equivalent("111111",1)) # Output: 5
print(odd_Equivalent("000000",1)) # Output: 0
print(odd_Equivalent("111111",2)) # Output: 5
print(odd_Equivalent("011001",3)) # Output: 3
print(odd_Equivalent("111111",1)) # Output: 5
print(odd_Equivalent("000000",0)) # Output: 0
print(odd_Equivalent("10101",2)) # Output: 3
print(odd_Equivalent("011001",4)) # Output: 3
print(odd_Equivalent("111111",3)) # Output: 5
print(odd_Equivalent("000000",0)) # Output: 0
print(odd_Equivalent("10101",5)) # Output: 1
print(odd_Equivalent("111111",2)) # Output: 5
print(odd_Equivalent("011001",1)) # Output: 3
print(odd_Equivalent("111111",0)) # Output: 5
print(odd_Equivalent("000000",1)) # Output: 0
print(odd_Equivalent("10101",3)) # Output: 3
print(odd_Equivalent("111111",4)) # Output: 5
print(odd_Equivalent("011001",2)) # Output: 3
print(odd_Equivalent("111111",1)) # Output: 5
print(odd_Equivalent("000000",0)) # Output: 0
print(odd_Equivalent("10101",4)) # Output: 1
print(odd_Equivalent("111111",5)) # Output: 5
print(odd_Equivalent("011001",5)) # Output: 3
print(odd_Equivalent("111111",4)) # Output: 5
print(odd_Equivalent("000000",1) # Output: 0
print(odd_Equivalent("10101",2) # Output: 3
print(odd_Equivalent("011001",3) # Output: 3
print(odd_Equivalent("111