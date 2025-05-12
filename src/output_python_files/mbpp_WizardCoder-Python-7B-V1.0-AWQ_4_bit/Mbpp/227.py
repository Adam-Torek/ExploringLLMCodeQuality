"""
Write a function to find minimum of three numbers.
assert min_of_three(10,20,0)==0
"""

def min_of_three(a,b,c):
    if a<b and a<c:
        return a
    elif b<a and b<c:
        return b
    else:
        return c

print(min_of_three(10,20,0)) # Output: 0
print(min_of_three(5,10,7)) # Output: 5
print(min_of_three(20,30,10)) # Output: 10
print(min_of_three(0,10,20)) # Output: 0
print(min_of_three(20,0,10)) # Output: 0
print(min_of_three(10,20,30)) # Output: 10
print(min_of_three(30,20,10)) # Output: 10
print(min_of_three(10,30,20)) # Output: 10
print(min_of_three(20,10,30)) # Output: 10
print(min_of_three(30,10,20)) # Output: 10
print(min_of_three(30,20,10)) # Output: 10
print(min_of_three(10,20,30)) # Output: 10
print(min_of_three(20,30,10)) # Output: 10
print(min_of_three(0,20,30)) # Output: 0
print(min_of_three(30,0,20)) # Output: 0
print(min_of_three(20,10,30)) # Output: 10
print(min_of_three(30,20,10)) # Output: 10
print(min_of_three(10,30,20)) # Output: 10
print(min_of_three(20,30,0)) # Output: 0
print(min_of_three(0,10,30)) # Output: 0
print(min_of_three(30,10,20)) # Output: 10
print(min_of_three(20,0,30)) # Output: 0
print(min_of_three(10,30,20)) # Output: 10
print(min_of_three(30,20,0)) # Output: 0
print(min_of_three(0,30,20)) # Output: 0
print(min_of_three(30,20,10)) # Output: 10
print(min_of_three(20,30,0)) # Output: 0
print(min_of_three(0,30,10)) # Output: 0
print(min_of_three(30,0,10)) # Output: 0
print(min_of_three(10,0,20)) # Output: 0
print(min_of_three(0,10,20) # Output: 0
print(min_of_three(0,20,10) # Output: 0
print(min_of_three(20,10,0) # Output: 0
print(min_of_three(10,0,30) # Output: 0
print(min_of_three(0,30,10) # Output: 0
print(min_of_three(30,10,0) # Output: 0
print(min_of_three(10,0,30) # Output: 0
print(min_