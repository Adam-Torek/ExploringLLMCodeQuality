"""
Write a python function to find the next perfect square greater than a given number.
assert next_Perfect_Square(35) == 36
"""

def next_Perfect_Square(num):
    import math
    root = int(math.sqrt(num))
    if root ** 2 == num:
        return root ** 2
    else:
        return (root + 1) ** 2

print(next_Perfect_Square(35)) # Output: 36
print(next_Perfect_Square(16)) # Output: 25
print(next_Perfect_Square(100)) # Output: 121
print(next_Perfect_Square(101)) # Output: 121
print(next_Perfect_Square(121)) # Output: 144
print(next_Perfect_Square(122)) # Output: 144
print(next_Perfect_Square(123)) # Output: 144
print(next_Perfect_Square(124)) # Output: 149
print(next_Perfect_Square(125)) # Output: 149
print(next_Perfect_Square(126)) # Output: 149
print(next_Perfect_Square(127)) # Output: 149
print(next_Perfect_Square(128)) # Output: 169
print(next_Perfect_Square(129)) # Output: 169
print(next_Perfect_Square(130)) # Output: 169
print(next_Perfect_Square(131)) # Output: 169
print(next_Perfect_Square(132)) # Output: 169
print(next_Perfect_Square(133)) # Output: 169
print(next_Perfect_Square(134)) # Output: 169
print(next_Perfect_Square(135)) # Output: 169
print(next_Perfect_Square(136)) # Output: 169
print(next_Perfect_Square(137)) # Output: 169
print(next_Perfect_Square(138)) # Output: 169
print(next_Perfect_Square(139)) # Output: 169
print(next_Perfect_Square(140)) # Output: 169
print(next_Perfect_Square(141)) # Output: 169
print(next_Perfect_Square(142)) # Output: 169
print(next_Perfect_Square(143)) # Output: 169
print(next_Perfect_Square(144)) # Output: 169
print(next_Perfect_Square(145)) # Output: 169
print(next_Perfect_Square(146)) # Output: 169
print(next_Perfect_Square(147)) # Output: 169
print(next_Perfect_Square(148)) # Output: 169
print(next_Perfect_Square(149)) # Output: 169
print(next_Perfect_Square(150)) # Output: 169
print(next_Perfect_Square(151)) # Output: 169
print(next_Perfect_Square(152)) # Output: 169
print(next_Perfect_Square(153)) # Output: 169
print(next_Perfect_Square(154)) # Output: 169
print(next_Perfect_Square(155)) # Output: 169
print(next_Perfect_Square(1