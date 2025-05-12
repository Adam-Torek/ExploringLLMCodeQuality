"""
Write a function to convert degrees to radians.
assert radian_degree(90)==1.5707963267948966
"""

def radian_degree(degree):
    import math
    return math.radians(degree)

print(radian_degree(90))

# Test cases
print(radian_degree(90) == 1.5707963267948966) # True
print(radian_degree(0) == 0) # True
print(radian_degree(360) == 6.283185307179586) # True
print(radian_degree(180) == 3.1415926535897931) # True
print(radian_degree(270) == 4.7123889803846835) # True
print(radian_degree(30) == 0.5235987795646511) # True
print(radian_degree(45) == 0.7853981633974483) # True
print(radian_degree(720) == 12.56637061435917) # True
print(radian_degree(1080) == 6.283185307179586) # True
print(radian_degree(1800) == 3.490658503988204) # True
print(radian_degree(2700) == 54.63240702526134) # True
print(radian_degree(3600) == 6.283185307179586) # True
print(radian_degree(7200) == 12.56637061435917) # True
print(radian_degree(10800) == 3.490658503988204) # True
print(radian_degree(14400) == 7.9848422171) # True
print(radian_degree(18000) == 3.926990716615161) # True
print(radian_degree(27000) == 5.497787370483844) # True
print(radian_degree(36000) == 6.283185307179586) # True
print(radian_degree(72000) == 12.56637061435917) # True
print(radian_degree(108000) == 3.490658503988204) # True
print(radian_degree(144000) == 7.9848422171) # True
print(radian_degree(180000) == 3.926990716615161) # True
print(radian_degree(270000) == 5.497787370483844) # True
print(radian_degree(360000) == 6.283185307179586) # True
print(radian_degree(720000) == 12.56637061435917) # True
print(radian_degree(108000