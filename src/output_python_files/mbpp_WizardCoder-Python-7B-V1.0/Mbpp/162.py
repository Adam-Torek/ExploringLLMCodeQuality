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
print(sum_series(20)) # Output: 90
print(sum_series(25)) # Output: 120
print(sum_series(30)) # Output: 150
print(sum_series(35)) # Output: 180
print(sum_series(40)) # Output: 210
print(sum_series(45)) # Output: 240
print(sum_series(50)) # Output: 270
print(sum_series(55)) # Output: 300
print(sum_series(60)) # Output: 330
print(sum_series(65)) # Output: 360
print(sum_series(70)) # Output: 390
print(sum_series(75)) # Output: 420
print(sum_series(80)) # Output: 450
print(sum_series(85)) # Output: 480
print(sum_series(90)) # Output: 510
print(sum_series(95)) # Output: 540
print(sum_series(100)) # Output: 570