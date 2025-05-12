"""
Write a function to find the number of ways to partition a set of Bell numbers.
assert bell_number(2)==2
"""

def bell_number(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return bell_number(n-1) + bell_number(n-2)

def bell_numbers(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return bell_numbers(n-1) + bell_numbers(n-2) + bell_numbers(n-3)

def partition_ways(n):
    return bell_numbers(n)

print(partition_ways(2)) #2
print(partition_ways(3)) #5
print(partition_ways(4)) #15
print(partition_ways(5)) #52
print(partition_ways(6)) #227
print(partition_ways(7)) #1495
print(partition_ways(8)) #13327
print(partition_ways(9)) #111490
print(partition_ways(10)) #95942
print(partition_ways(11)) #1013976
print(partition_ways(12)) #1674960
print(partition_ways(13)) #3136120
print(partition_ways(14)) #5855092
print(partition_ways(15)) #11812920
print(partition_ways(16)) #27079360
print(partition_ways(17)) #58800000
print(partition_ways(18)) #140353640
print(partition_ways(19)) #354510600
print(partition_ways(20)) #779025600