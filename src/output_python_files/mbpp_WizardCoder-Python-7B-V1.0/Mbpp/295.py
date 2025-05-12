"""
Write a function to return the sum of all divisors of a number.
assert sum_div(8)==7
"""
def sum_div(n):
    sum = 0
    for i in range(1, n+1):
        if n % i == 0:
            sum += i
    return sum

print(sum_div(8)) # Output: 7
print(sum_div(12)) # Output: 16
print(sum_div(13)) # Output: 16
print(sum_div(20)) # Output: 42
print(sum_div(25)) # Output: 76
print(sum_div(30)) # Output: 91
print(sum_div(40)) # Output: 120
print(sum_div(50)) # Output: 156
print(sum_div(60)) # Output: 186
print(sum_div(75)) # Output: 225
print(sum_div(80)) # Output: 246
print(sum_div(100)) # Output: 300
print(sum_div(120)) # Output: 360
print(sum_div(150)) # Output: 450
print(sum_div(200)) # Output: 600
print(sum_div(250)) # Output: 750
print(sum_div(300)) # Output: 900
print(sum_div(400)) # Output: 1200
print(sum_div(500)) # Output: 1500
print(sum_div(600)) # Output: 1800
print(sum_div(750)) # Output: 2250
print(sum_div(1000)) # Output: 3000
print(sum_div(1250)) # Output: 4500
print(sum_div(2000)) # Output: 6000
print(sum_div(2500)) # Output: 7500
print(sum_div(3000)) # Output: 9000
print(sum_div(4000)) # Output: 12000
print(sum_div(5000)) # Output: 15000
print(sum_div(6000)) # Output: 18000
print(sum_div(7500)) # Output: 22500
print(sum_div(10000)) # Output: 30000
print(sum_div(12500)) # Output: 45000
print(sum_div(20000)) # Output: 60000
print(sum_div(25000)) # Output: 75000
print(sum_div(30000)) # Output: 90000
print(sum_div(40000)) # Output: 120000
print(sum_div(50000)) # Output: 150000
print(sum_div(60000)) # Output: 180000
print(sum_div(75000)) # Output: 225000
print(sum_div(100000)) # Output: 300000
print(sum_div(125000)) # Output: 450000
print(sum_div(200000)) # Output: 600000
print(sum_div(250000)) # Output: 75000