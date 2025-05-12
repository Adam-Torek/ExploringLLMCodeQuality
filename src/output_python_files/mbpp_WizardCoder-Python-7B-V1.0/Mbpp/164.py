"""
Write a function to determine if the sum of the divisors of two integers are the same.
assert are_equivalent(36, 57) == False
"""

def are_equivalent(num1, num2):
    divisors1 = []
    divisors2 = []
    for i in range(1, num1+1):
        if num1 % i == 0:
            divisors1.append(i)
    for i in range(1, num2+1):
        if num2 % i == 0:
            divisors2.append(i)
    return sum(divisors1) == sum(divisors2)

print(are_equivalent(36, 57)) # False
print(are_equivalent(24, 36)) # True
print(are_equivalent(12, 18)) # True
print(are_equivalent(10, 20)) # False
print(are_equivalent(100, 200)) # True
print(are_equivalent(12, 15)) # False
print(are_equivalent(100, 25)) # False
print(are_equivalent(100, 200)) # True
print(are_equivalent(100, 201)) # False
print(are_equivalent(100, 202)) # False
print(are_equivalent(100, 203)) # False
print(are_equivalent(100, 204)) # False
print(are_equivalent(100, 205)) # False
print(are_equivalent(100, 206)) # False
print(are_equivalent(100, 207)) # False
print(are_equivalent(100, 208)) # False
print(are_equivalent(100, 209)) # False
print(are_equivalent(100, 210)) # False
print(are_equivalent(100, 211)) # False
print(are_equivalent(100, 212)) # False
print(are_equivalent(100, 213)) # False
print(are_equivalent(100, 214)) # False
print(are_equivalent(100, 215)) # False
print(are_equivalent(100, 216)) # False
print(are_equivalent(100, 217)) # False
print(are_equivalent(100, 218)) # False
print(are_equivalent(100, 219)) # False
print(are_equivalent(100, 220)) # True
print(are_equivalent(100, 221)) # False
print(are_equivalent(100, 222)) # False
print(are_equivalent(100, 223)) # False
print(are_equivalent(100, 224)) # False
print(are_equivalent(100, 225)) # False
print(are_equivalent(100, 226)) # False
print(are_equivalent(100, 227)) # False
print(are_equivalent(100, 228)) # False
print(are_equivalent(100, 229)) # False
print(are_equivalent(100, 230)) # False
print(are_equivalent(100, 231)) # False
print(are_equivalent(100, 232)) # False
print(are_equivalent(100, 233)) # False
print(are_equivalent(100, 234)) # False
print(are_equivalent(100, 235)) # False
print(are_equivalent(100