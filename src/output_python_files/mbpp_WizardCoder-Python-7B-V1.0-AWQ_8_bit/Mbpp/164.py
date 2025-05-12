"""
Write a function to determine if the sum of the divisors of two integers are the same.
assert are_equivalent(36, 57) == False
"""

def are_equivalent(a, b):
    divisors_a = [i for i in range(1, a+1) if a % i == 0]
    divisors_b = [i for i in range(1, b+1) if b % i == 0]
    return sum(divisors_a) == sum(divisors_b)

print(are_equivalent(36, 57)) # False
print(are_equivalent(12, 18)) # True
print(are_equivalent(10, 20)) # True
print(are_equivalent(10, 25)) # False
print(are_equivalent(10, 30)) # True
print(are_equivalent(10, 36)) # True
print(are_equivalent(10, 40)) # False
print(are_equivalent(10, 45)) # True
print(are_equivalent(10, 50)) # True
print(are_equivalent(10, 54)) # False
print(are_equivalent(10, 60)) # True
print(are_equivalent(10, 66)) # False
print(are_equivalent(10, 70)) # True
print(are_equivalent(10, 75)) # False
print(are_equivalent(10, 80)) # True
print(are_equivalent(10, 85)) # False
print(are_equivalent(10, 90)) # True
print(are_equivalent(10, 95)) # False
print(are_equivalent(10, 100)) # True
print(are_equivalent(10, 105)) # False
print(are_equivalent(10, 110)) # True
print(are_equivalent(10, 115)) # False
print(are_equivalent(10, 120)) # True
print(are_equivalent(10, 125)) # False
print(are_equivalent(10, 130)) # True
print(are_equivalent(10, 135)) # False
print(are_equivalent(10, 140)) # True
print(are_equivalent(10, 145)) # False
print(are_equivalent(10, 150)) # True
print(are_equivalent(10, 155)) # False
print(are_equivalent(10, 160)) # True
print(are_equivalent(10, 165)) # False
print(are_equivalent(10, 170)) # True
print(are_equivalent(10, 175)) # False
print(are_equivalent(10, 180)) # True
print(are_equivalent(10, 185)) # False
print(are_equivalent(10, 190)) # True
print(are_equivalent(10, 195)) # False
print(are_equivalent(10, 200)) # True
print(are_equivalent(10, 205)) # False
print(are_equivalent(10, 210)) # True
print(are_equivalent(10, 215)) # False
print(are_equivalent(10, 220)) # True
print(are_equivalent(10, 225)) # False
print(are_equivalent(10, 230)) # True
print(are_equivalent(10, 235)) # False
print(are_equivalent(10, 240)) # True
print(are_equivalent(10, 245)) # False
print(are_equivalent(10, 250)) # True
print(are_equivalent(10, 255)) # False
print(are_equivalent(10,