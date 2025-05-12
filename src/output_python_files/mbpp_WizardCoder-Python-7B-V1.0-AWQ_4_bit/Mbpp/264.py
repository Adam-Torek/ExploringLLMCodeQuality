"""
Write a function to calculate a dog's age in dog's years.
assert dog_age(12)==61
"""

def dog_age(human_age):
    return human_age*7

print(dog_age(12))

# Test cases
assert dog_age(12) == 61
assert dog_age(2) == 14
assert dog_age(10) == 70
assert dog_age(5) == 35
assert dog_age(1) == 7
assert dog_age(0) == 0
assert dog_age(100) == 700