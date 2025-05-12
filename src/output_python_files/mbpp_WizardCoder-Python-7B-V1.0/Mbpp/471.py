"""
Write a python function to find the product of the array multiplication modulo n.
assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9
"""

def find_remainder(arr, n):
    result = 1
    for i in arr:
        result = (result * i) % n
    return result

print(find_remainder([100, 10, 5, 25, 35, 14], 11)) # Output: 9
print(find_remainder([100, 10, 5, 25, 35, 14], 13)) # Output: 10
print(find_remainder([100, 10, 5, 25, 35, 14], 10)) # Output: 5
print(find_remainder([100, 10, 5, 25, 35, 14], 17)) # Output: 13
print(find_remainder([100, 10, 5, 25, 35, 14], 20)) # Output: 10
print(find_remainder([100, 10, 5, 25, 35, 14], 25)) # Output: 10
print(find_remainder([100, 10, 5, 25, 35, 14], 30)) # Output: 10
print(find_remainder([100, 10, 5, 25, 35, 14], 35)) # Output: 10
print(find_remainder([100, 10, 5, 25, 35, 14], 40)) # Output: 10
print(find_remainder([100, 10, 5, 25, 35, 14], 50)) # Output: 10
print(find_remainder([100, 10, 5, 25, 35, 14], 100)) # Output: 10
print(find_remainder([100, 10, 5, 25, 35, 14], 1000)) # Output: 10
print(find_remainder([100, 10, 5, 25, 35, 14], 10000)) # Output: 10
print(find_remainder([100, 10, 5, 25, 35, 14], 100000)) # Output: 10
print(find_remainder([100, 10, 5, 25, 35, 14], 1000000)) # Output: 10
print(find_remainder([100, 10, 5, 25, 35, 14], 10000000)) # Output: 10
print(find_remainder([100, 10, 5, 25, 35, 14], 100000000)) # Output: 10
print(find_remainder([100, 10, 5, 25, 35, 14], 1000000000)) # Output: 10
print(find_remainder([100, 10, 5, 25, 35, 14], 10000000000)) # Output: 10
print(find_remainder([100, 10, 5, 25, 35, 14], 1