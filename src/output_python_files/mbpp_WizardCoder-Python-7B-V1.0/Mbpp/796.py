"""
Write function to find the sum of all items in the given dictionary.
assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
"""

def return_sum(dictionary):
    sum = 0
    for value in dictionary.values():
        sum += value
    return sum

print(return_sum({'a': 100, 'b':200, 'c':300})) # Output: 600
print(return_sum({'a': 100, 'b':200, 'c':300, 'd':400, 'e':500})) # Output: 1500
print(return_sum({'a': 100, 'b':200, 'c':300, 'd':400, 'e':500, 'f':600})) # Output: 2100
print(return_sum({'a': 100, 'b':200, 'c':300, 'd':400, 'e':500, 'f':600, 'g':700})) # Output: 3100
print(return_sum({'a': 100, 'b':200, 'c':300, 'd':400, 'e':500, 'f':600, 'g':700, 'h':800})) # Output: 4100
print(return_sum({'a': 100, 'b':200, 'c':300, 'd':400, 'e':500, 'f':600, 'g':700, 'h':800, 'i':900})) # Output: 5100
print(return_sum({'a': 100, 'b':200, 'c':300, 'd':400, 'e':500, 'f':600, 'g':700, 'h':800, 'i':900, 'j':1000})) # Output: 6100

# Test cases
# Test case 1:
# Input: {'a': 100, 'b':200, 'c':300}
# Output: 600

# Test case 2:
# Input: {'a': 100, 'b':200, 'c':300, 'd':400, 'e':500}
# Output: 1500

# Test case 3:
# Input: {'a': 100, 'b':200, 'c':300, 'd':400, 'e':500, 'f':600}
# Output: 2100

# Test case 4:
# Input: {'a': 100, 'b':200, 'c':300, 'd':400, 'e':500, 'f':600, 'g':700}
# Output: 3100

# Test case 5:
# Input: {'a': 100, 'b':200, 'c':300, 'd':400, 'e':500, 'f':600, 'g':700, 'h':800}
# Output: 4100

# Test case 6:
# Input: {'a': 100, 'b':200, 'c':300, 'd':400, 'e':500, 'f':600, 'g':700, 'h':800, 'i':900}
# Output: 5100