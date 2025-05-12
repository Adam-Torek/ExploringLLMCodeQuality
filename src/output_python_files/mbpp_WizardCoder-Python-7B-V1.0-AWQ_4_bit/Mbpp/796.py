"""
Write function to find the sum of all items in the given dictionary.
assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
"""

def return_sum(d):
    total = 0
    for value in d.values():
        total += value
    return total

print(return_sum({'a': 100, 'b':200, 'c':300})) # Output: 600
print(return_sum({'a': 10, 'b':20, 'c':30})) # Output: 60
print(return_sum({'a': 10, 'b':20, 'c':30, 'd':40, 'e':50})) # Output: 100
print(return_sum({'a': 10, 'b':20, 'c':30, 'd':40, 'e':50, 'f':60, 'g':70, 'h':80, 'i':90})) # Output: 300

# Test cases
# print(return_sum({'a': 100, 'b':200, 'c':300})) # Output: 600
# print(return_sum({'a': 10, 'b':20, 'c':30})) # Output: 60
# print(return_sum({'a': 10, 'b':20, 'c':30, 'd':40, 'e':50})) # Output: 100
# print(return_sum({'a': 10, 'b':20, 'c':30, 'd':40, 'e':50, 'f':60, 'g':70, 'h':80, 'i':90})) # Output: 300

# Test cases
# print(return_sum({'a': 100, 'b':200, 'c':300, 'd':400, 'e':500, 'f':600, 'g':700, 'h':800, 'i':900, 'j':1000, 'k':1100, 'l':1200, 'm':1300, 'n':1400, 'o':1500, 'p':1600, 'q':1700, 'r':1800, 's':1900, 't':2000, 'u':2100, 'v':2200, 'w':2300, 'x':2400, 'y':2500, 'z':2600})) # Output: 9100
# print(return_sum({'a': 10, 'b':20, 'c':30, 'd':40, 'e':50, 'f':60, 'g':70, 'h':80, 'i':90, 'j':100, 'k':110, 'l':120, 'm':130, 'n':140, 'o':150, 'p':160, 'q':170, 'r':180, 's':190, 't':200, 'u':210, 'v':220, 'w':230, 'x':240, 'y':250, 'z':260})) # Output: 1000
# print(return_sum({'a': 10, 'b':20, 'c':30, 'd':40, 'e':50, 'f':60, 'g':70, 'h':80, 'i':90, 'j':100, 'k':110, 'l':120, 'm':130, 'n':140, 'o':150, 'p':160, 'q':170, 'r':180, 's':190, 't':200, 'u':210, 'v':220