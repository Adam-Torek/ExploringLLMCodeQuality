"""
Write a function to find nth polite number. geeksforgeeks.org/n-th-polite-number/
assert is_polite(7) == 11
"""

def is_polite(n):
    """
    Check if n is polite number
    """
    digits = [int(d) for d in str(n)]
    return sum(digit * (len(digits) - i) for i, digit in enumerate(digits)) == n

def polite_number(n):
    """
    Find nth polite number
    """
    polite_num = 0
    count = 0
    while count < n:
        polite_num += 1
        if is_polite(polite_num):
            count += 1
    return polite_num

if __name__ == "__main__":
    n = int(input())
    print(polite_number(n))