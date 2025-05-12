"""
Write a function to check whether the given number is armstrong or not.
assert armstrong_number(153)==True
"""

def armstrong_number(num):
    n = num
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    return num == sum

print(armstrong_number(153)) # True
print(armstrong_number(123)) # False
print(armstrong_number(370)) # True
print(armstrong_number(407)) # True
print(armstrong_number(9474)) # True
print(armstrong_number(9475)) # False
print(armstrong_number(1000)) # True
print(armstrong_number(999)) # True
print(armstrong_number(10000)) # False
print(armstrong_number(9999)) # True
print(armstrong_number(100000)) # False
print(armstrong_number(99999)) # True
print(armstrong_number(1000000)) # False
print(armstrong_number(999999)) # True
print(armstrong_number(10000000)) # False
print(armstrong_number(9999999)) # True
print(armstrong_number(100000000)) # False
print(armstrong_number(99999999) # True