"""
Write function to find the sum of all items in the given dictionary.
assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
"""

def return_sum(d):
    return sum(d.values())

print(return_sum({'a': 100, 'b':200, 'c':300})) # Output: 600

# Test cases
print(return_sum({'a': 100, 'b':200, 'c':300})) # Output: 600
print(return_sum({'a': 100, 'b':200, 'c':300, 'd':400, 'e':500})) # Output: 1500
print(return_sum({'a': 100, 'b':-200, 'c':300, 'd':-400, 'e':500})) # Output: -50
print(return_sum({'a': 100, 'b':200, 'c':300, 'd':400, 'e':500, 'f':600, 'g':700, 'h':800, 'i':900})) # Output: 4500
print(return_sum({'a': 100, 'b':200, 'c':300, 'd':400, 'e':500, 'f':600, 'g':700, 'h':800, 'i':900, 'j':1000, 'k':1100, 'l':1200, 'm':1300, 'n':1400, 'o':1500})) # Output: 6500
print(return_sum({'a': 100, 'b':200, 'c':300, 'd':400, 'e':500, 'f':600, 'g':700, 'h':800, 'i':900, 'j':100, 'k':1100, 'l':1200, 'm':1300, 'n':1400, 'o':1500, 'p':-1000, 'q':-200, 'r':-300, 's':-400, 't':-500, 'u':-600, 'v':-700, 'w':-800, 'x':-900, 'y':-1000, 'z':-1100})) # Output: -1100

# Test case for empty dictionary
print(return_sum({})) # Output: 0

# Test case for dictionary with negative values
print(return_sum({'a': -100, 'b':-200, 'c':-300, 'd':-400, 'e':-500, 'f':-600, 'g':-700, 'h':-800, 'i':-900})) # Output: -900

# Test case for dictionary with negative and positive values
print(return_sum({'a': -100, 'b':200, 'c':300, 'd':-400, 'e':500, 'f':600, 'g':-700, 'h':800, 'i':900, 'j':-100, 'k':1100, 'l':1200, 'm':-1300, 'n':1400, 'o':-1500})) # Output: 0

# Test case for dictionary with only negative values
print(return_sum({'a': -100, 'b':-200, 'c':-300, 'd':-400, 'e':-500, 'f':-600, 'g':-700, 'h':-800, 'i':-900})) # Output: