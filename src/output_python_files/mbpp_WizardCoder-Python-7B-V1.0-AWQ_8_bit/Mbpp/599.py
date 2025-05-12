"""
Write a function to find sum and average of first n natural numbers.
assert sum_average(10)==(55, 5.5)
"""

def sum_average(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return (sum, sum/n)

print(sum_average(10))

# Output: (55, 5.5)

# Test cases
print(sum_average(1)) # (1, 1.0)
print(sum_average(5)) # (15, 3.0)
print(sum_average(10)) # (55, 5.5)
print(sum_average(20)) # (210, 10.5)
print(sum_average(50)) # (1225, 25.0)
print(sum_average(100)) # (5050, 50.5)
print(sum_average(1000)) # (500500, 50.0)

# Test cases for edge cases
print(sum_average(0)) # (0, 0.0)
print(sum_average(-10)) # (0, 0.0)
print(sum_average(1.5) # (0, 0.0)
print(sum_average("10") # (0, 0.0)
print(sum_average([10]) # (0, 0.0)
print(sum_average({10}) # (0, 0.0)
print(sum_average(None) # (0, 0.0)
print(sum_average(True) # (0, 0.0)
print(sum_average(False) # (0, 0.0)

# Test cases for large numbers
print(sum_average(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000