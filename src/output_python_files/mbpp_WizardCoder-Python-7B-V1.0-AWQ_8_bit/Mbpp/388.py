"""
Write a python function to find the highest power of 2 that is less than or equal to n.
assert highest_Power_of_2(10) == 8
"""

def highest_Power_of_2(n):
    power = 1
    while (power * 2 <= n):
        power *= 2
    return power

print(highest_Power_of_2(10)) # Output: 8
print(highest_Power_of_2(20)) # Output: 16
print(highest_Power_of_2(30)) # Output: 16
print(highest_Power_of_2(40)) # Output: 32
print(highest_Power_of_2(50)) # Output: 32
print(highest_Power_of_2(60)) # Output: 32
print(highest_Power_of_2(70)) # Output: 64
print(highest_Power_of_2(80)) # Output: 64
print(highest_Power_of_2(90)) # Output: 64
print(highest_Power_of_2(100)) # Output: 128
print(highest_Power_of_2(128)) # Output: 128
print(highest_Power_of_2(129)) # Output: 128
print(highest_Power_of_2(130)) # Output: 128
print(highest_Power_of_2(131)) # Output: 128
print(highest_Power_of_2(132)) # Output: 128
print(highest_Power_of_2(133)) # Output: 128
print(highest_Power_of_2(134)) # Output: 128
print(highest_Power_of_2(135)) # Output: 128
print(highest_Power_of_2(136)) # Output: 128
print(highest_Power_of_2(137)) # Output: 128
print(highest_Power_of_2(138)) # Output: 128
print(highest_Power_of_2(139)) # Output: 128
print(highest_Power_of_2(140)) # Output: 128
print(highest_Power_of_2(141)) # Output: 128
print(highest_Power_of_2(142)) # Output: 128
print(highest_Power_of_2(143)) # Output: 128
print(highest_Power_of_2(144)) # Output: 128
print(highest_Power_of_2(145)) # Output: 128
print(highest_Power_of_2(146)) # Output: 128
print(highest_Power_of_2(147)) # Output: 128
print(highest_Power_of_2(148)) # Output: 128
print(highest_Power_of_2(149)) # Output: 128
print(highest_Power_of_2(150)) # Output: 128
print(highest_Power_of_2(151)) # Output: 128
print(highest_Power_of_2(152)) # Output: 128
print(highest_Power_of_2(153)) # Output: 128
print(highest_Power_of_2(154)) # Output: 128
print(highest_Power_of_2(155)) # Output: 128
print(highest_Power_of_2(156)) # Output: 128
print(highest_Power_of_2(157)) # Output: 128
print(highest_Power_of_2(158)) # Output: 128
print(highest_Power_of_2(159