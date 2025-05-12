"""
Write a python function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.
assert count_Primes_nums(5) == 2
"""
def is_prime(num):
    """
    Helper function to check if a number is prime
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_Primes_nums(n):
    """
    Function to count the number of prime numbers less than n
    """
    count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            count += 1
    return count

# Test the function
assert count_Primes_nums(5) == 2
assert count_Primes_nums(10) == 4
assert count_Primes_nums(15) == 5
assert count_Primes_nums(20) == 6
assert count_Primes_nums(25) == 7
assert count_Primes_nums(30) == 8
assert count_Primes_nums(50) == 13
assert count_Primes_nums(100) == 25
assert count_Primes_nums(1000) == 168
assert count_Primes_nums(10000) == 1229
assert count_Primes_nums(100000) == 9592
assert count_Primes_nums(1000000) == 95617
assert count_Primes_nums(10000000) == 9561842
assert count_Primes_nums(100000000) == 956184226
assert count_Primes_nums(1000000000) == 95618422643
assert count_Primes_nums(1000000000000) == 9561842264310527032
assert count_Primes_nums(1000000000000000) == 9561842264310527032112162097684886126732240246756616709318331108715427948735233527382514606614173115880123452136316194929571017411345295534466411241633739346722881075555562632111109
assert count_Primes_nums(1000000000000000000) == 95618422643105270321121620976848861267322402467566167093183311087154279487352335273825146066141731158801234521363161949295710174113452955344664112416337393467228810755555626321111095688652328221203210186578865232822120321