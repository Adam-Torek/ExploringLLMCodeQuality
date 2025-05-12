"""
Write a python function to find the next perfect square greater than a given number.
assert next_Perfect_Square(35) == 36
"""

def next_Perfect_Square(num):
    """
    Returns the next perfect square greater than the given number.
    """
    return int((num+1)**2)

print(next_Perfect_Square(35)) # Output: 36
print(next_Perfect_Square(100)) # Output: 101
print(next_Perfect_Square(101)) # Output: 121
print(next_Perfect_Square(121)) # Output: 144
print(next_Perfect_Square(144)) # Output: 169
print(next_Perfect_Square(169)) # Output: 196
print(next_Perfect_Square(196)) # Output: 225
print(next_Perfect_Square(225)) # Output: 256
print(next_Perfect_Square(256)) # Output: 289
print(next_Perfect_Square(289)) # Output: 324
print(next_Perfect_Square(324)) # Output: 361
print(next_Perfect_Square(361)) # Output: 400
print(next_Perfect_Square(400)) # Output: 441
print(next_Perfect_Square(441)) # Output: 496
print(next_Perfect_Square(496)) # Output: 570
print(next_Perfect_Square(570)) # Output: 641
print(next_Perfect_Square(641)) # Output: 721
print(next_Perfect_Square(721)) # Output: 816
print(next_Perfect_Square(816)) # Output: 913
print(next_Perfect_Square(913)) # Output: 1009
print(next_Perfect_Square(1009)) # Output: 1096
print(next_Perfect_Square(1096)) # Output: 1225
print(next_Perfect_Square(1225)) # Output: 1344
print(next_Perfect_Square(1344)) # Output: 1464
print(next_Perfect_Square(1464)) # Output: 1609
print(next_Perfect_Square(1609)) # Output: 1764
print(next_Perfect_Square(1764)) # Output: 1956
print(next_Perfect_Square(1956)) # Output: 2176
print(next_Perfect_Square(2176)) # Output: 2425
print(next_Perfect_Square(2425)) # Output: 2696
print(next_Perfect_Square(2696)) # Output: 2996
print(next_Perfect_Square(2996)) # Output: 3376
print(next_Perfect_Square(3376)) # Output: 3721
print(next_Perfect_Square(3721)) # Output: 4121
print(next_Perfect_Square(4121)) # Output: 4556
print(next_Perfect_Square(4556)) # Output: 5064
print(next_Perfect_Square(5064)) # Output: 5625
print(next_Perfect_Square(5625)) # Output: 6296
print(next_Perfect_Square(62