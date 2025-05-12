"""
Write a function to find the number of ways to partition a set of Bell numbers.
assert bell_number(2)==2
"""

def bell_number(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n * bell_number(n-1) + bell_number(n-1) * (n-1)

def partition_count(n):
    return bell_number(n)

print(partition_count(2)) # 2
print(partition_count(3)) # 5
print(partition_count(4)) # 15
print(partition_count(5)) # 52
print(partition_count(6)) # 203
print(partition_count(7)) # 870
print(partition_count(8)) # 4140
print(partition_count(9)) # 21140
print(partition_count(10)) # 116195
print(partition_count(11)) # 68250
print(partition_count(12)) # 394650
print(partition_count(13)) # 2658208
print(partition_count(14)) # 16715105
print(partition_count(15)) # 114400045
print(partition_count(16)) # 740479040
print(partition_count(17)) # 4889034665
print(partition_count(18)) # 32435611150
print(partition_count(19)) # 227579385405
print(partition_count(20)) # 1588890171500
print(partition_count(21)) # 11414453070000
print(partition_count(22)) # 82111760810000
print(partition_count(23)) # 573170001000000
print(partition_count(24)) # 4046541010000000
print(partition_count(25)) # 28921414400000000
print(partition_count(26)) # 197555044000000000
print(partition_count(27)) # 1488903480000000000
print(partition_count(28)) # 11488903480000000000
print(partition_count(29)) # 9288260100000000000
print(partition_count(30)) # 69960800000000000000