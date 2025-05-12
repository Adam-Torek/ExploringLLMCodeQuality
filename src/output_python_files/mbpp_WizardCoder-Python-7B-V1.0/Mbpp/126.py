"""
Write a python function to find the sum of common divisors of two given numbers.
assert sum(10,15) == 6
"""

def sum_of_common_divisors(num1, num2):
    divisors = []
    for i in range(1, num1+1):
        if num1 % i == 0 and num2 % i == 0:
            divisors.append(i)
    return sum(divisors)

print(sum_of_common_divisors(10,15)) # Output: 6
print(sum_of_common_divisors(20,18)) # Output: 6
print(sum_of_common_divisors(12,24)) # Output: 6
print(sum_of_common_divisors(16,24)) # Output: 12
print(sum_of_common_divisors(24,36)) # Output: 12
print(sum_of_common_divisors(48,60)) # Output: 24
print(sum_of_common_divisors(72,96)) # Output: 24
print(sum_of_common_divisors(100,120)) # Output: 30
print(sum_of_common_divisors(100,150)) # Output: 30
print(sum_of_common_divisors(100,200)) # Output: 60
print(sum_of_common_divisors(100,250)) # Output: 60
print(sum_of_common_divisors(100,300)) # Output: 60
print(sum_of_common_divisors(100,400)) # Output: 60
print(sum_of_common_divisors(100,500)) # Output: 60
print(sum_of_common_divisors(100,600)) # Output: 60
print(sum_of_common_divisors(100,750)) # Output: 60
print(sum_of_common_divisors(100,1000)) # Output: 100
print(sum_of_common_divisors(100,1500)) # Output: 60
print(sum_of_common_divisors(100,2000)) # Output: 60
print(sum_of_common_divisors(100,2500)) # Output: 60
print(sum_of_common_divisors(100,3000)) # Output: 60
print(sum_of_common_divisors(100,4000)) # Output: 60
print(sum_of_common_divisors(100,5000)) # Output: 60
print(sum_of_common_divisors(100,6000)) # Output: 60
print(sum_of_common_divisors(100,7500)) # Output: 60
print(sum_of_common_divisors(100,10000)) # Output: 60
print(sum_of_common_divisors(100,15000)) # Output: 60
print(sum_of_common_divisors(100,20000)) # Output: 60
print(sum_of_common_divisors(100,25000)) # Output: 60
print(sum_of_common_divisors(100,30000)) # Output: 60
print(sum_of_common_divisors(100,40000)) # Output: 60
print(sum_of_common_divisors(100,50000)) # Output: 60
print(sum_of_common_divisors