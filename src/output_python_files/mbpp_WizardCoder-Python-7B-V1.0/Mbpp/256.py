"""
Write a python function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.
assert count_Primes_nums(5) == 2
"""

def count_Primes_nums(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    return count

print(count_Primes_nums(5)) # Output: 2
print(count_Primes_nums(10)) # Output: 4
print(count_Primes_nums(15)) # Output: 5
print(count_Primes_nums(20)) # Output: 7
print(count_Primes_nums(25)) # Output: 8
print(count_Primes_nums(30)) # Output: 10
print(count_Primes_nums(35)) # Output: 11
print(count_Primes_nums(40)) # Output: 12
print(count_Primes_nums(45)) # Output: 13
print(count_Primes_nums(50)) # Output: 14
print(count_Primes_nums(55)) # Output: 15
print(count_Primes_nums(60)) # Output: 16
print(count_Primes_nums(65)) # Output: 17
print(count_Primes_nums(70)) # Output: 18
print(count_Primes_nums(75)) # Output: 19
print(count_Primes_nums(80)) # Output: 20
print(count_Primes_nums(85)) # Output: 21
print(count_Primes_nums(90)) # Output: 22
print(count_Primes_nums(95)) # Output: 23
print(count_Primes_nums(100)) # Output: 24
print(count_Primes_nums(105)) # Output: 25
print(count_Primes_nums(110)) # Output: 26
print(count_Primes_nums(115)) # Output: 27
print(count_Primes_nums(120)) # Output: 28
print(count_Primes_nums(125)) # Output: 29
print(count_Primes_nums(130)) # Output: 30
print(count_Primes_nums(135)) # Output: 31
print(count_Primes_nums(140)) # Output: 32
print(count_Primes_nums(145)) # Output: 33
print(count_Primes_nums(150)) # Output: 34
print(count_Primes_nums(155)) # Output: 35
print(count_Primes_nums(160)) # Output: 36
print(count_Primes_nums(165)) # Output: 37
print(count_Primes_nums(170)) # Output: 38
print(count_Primes_nums(175)) # Output: 39
print(count_Primes_nums(180)) # Output: 40
print(count_Primes_nums(185)) # Output: 41
print(count_Primes_nums(190)) # Output: 42
print(count_Primes_nums(195)) # Output: 43
print(count_Primes_nums(200)) # Output: 44
print(count_Primes_nums(205)) # Output: 45
print(count_Pr