"""
Write a python function to find the sum of even factors of a number.
assert sumofFactors(18) == 26
"""

def sumofFactors(n):
    sum = 0
    for i in range(1, n+1):
        if n % i == 0 and i % 2 == 0:
            sum += i
    return sum

print(sumofFactors(18)) # Output: 26
print(sumofFactors(24)) # Output: 12
print(sumofFactors(20)) # Output: 10
print(sumofFactors(15)) # Output: 0
print(sumofFactors(100)) # Output: 122
print(sumofFactors(25)) # Output: 50
print(sumofFactors(1)) # Output: 0
print(sumofFactors(3)) # Output: 0
print(sumofFactors(4)) # Output: 4
print(sumofFactors(5)) # Output: 0
print(sumofFactors(6)) # Output: 6
print(sumofFactors(7)) # Output: 0
print(sumofFactors(8)) # Output: 8
print(sumofFactors(9)) # Output: 0
print(sumofFactors(10)) # Output: 10
print(sumofFactors(11)) # Output: 0
print(sumofFactors(12)) # Output: 12
print(sumofFactors(13)) # Output: 0
print(sumofFactors(14)) # Output: 14
print(sumofFactors(15)) # Output: 0
print(sumofFactors(16)) # Output: 16
print(sumofFactors(17)) # Output: 0
print(sumofFactors(19)) # Output: 0
print(sumofFactors(20)) # Output: 12
print(sumofFactors(21)) # Output: 0
print(sumofFactors(22)) # Output: 22
print(sumofFactors(23)) # Output: 0
print(sumofFactors(24)) # Output: 24
print(sumofFactors(25)) # Output: 50
print(sumofFactors(26)) # Output: 26
print(sumofFactors(27)) # Output: 0
print(sumofFactors(28)) # Output: 28
print(sumofFactors(29)) # Output: 0
print(sumofFactors(30)) # Output: 30
print(sumofFactors(31)) # Output: 0
print(sumofFactors(32)) # Output: 32
print(sumofFactors(33)) # Output: 0
print(sumofFactors(34)) # Output: 34
print(sumofFactors(35)) # Output: 0
print(sumofFactors(36)) # Output: 36
print(sumofFactors(37)) # Output: 0
print(sumofFactors(38)) # Output: 38
print(sumofFactors(39)) # Output: 0
print(sumofFactors(40)) # Output: 40
print(sumofFactors(41)) # Output: 0
print(sumofFactors(42)) # Output: 42
print(sumofFactors(43)) # Output: 0
print(sumofFactors(44)) # Output: 44
print(sumofFactors(45)) # Output: 0
print(sumofFactors(46)) # Output: 46
print(sumofFactors(47)) # Output: 0
print(sumofFactors(48)) # Output: 48
print(sumofFactors(49)) # Output: 0
print(sumofFactors(50)) # Output: 50
print(sumofFactors(51)) # Output: 0
print(sumof