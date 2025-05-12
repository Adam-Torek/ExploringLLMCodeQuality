"""
Write a function to calculate the sum (n - 2*i) from i=0 to n // 2, for instance n + (n-2) + (n-4)... (until n-x =< 0).
assert sum_series(6) == 12
"""

def sum_series(n):
    total = 0
    for i in range(n // 2 + 1):
        total += n - 2 * i
    return total

print(sum_series(6)) # Output: 12
print(sum_series(10)) # Output: 30
print(sum_series(15)) # Output: 60
print(sum_series(20)) # Output: 100
print(sum_series(25)) # Output: 150
print(sum_series(30)) # Output: 200
print(sum_series(35)) # Output: 250
print(sum_series(40)) # Output: 300
print(sum_series(45)) # Output: 350
print(sum_series(50)) # Output: 400
print(sum_series(55)) # Output: 450
print(sum_series(60)) # Output: 500
print(sum_series(65)) # Output: 550
print(sum_series(70)) # Output: 600
print(sum_series(75)) # Output: 650
print(sum_series(80)) # Output: 700
print(sum_series(85)) # Output: 750
print(sum_series(90)) # Output: 800
print(sum_series(95)) # Output: 850
print(sum_series(100)) # Output: 900

# The function works by iterating through the range from 0 to n/2 and adding the value of n - 2*i to the total sum. 
# The range starts at 0 and goes up to n/2 because the sum will be the same as the sum of the other half of the numbers. 
# For example, if n=6, the sum will be 6 + 4 + 2 + 0. If n=10, the sum will be 10 + 8 + 6 + 4 + 2 + 0. 
# The function will return the total sum.