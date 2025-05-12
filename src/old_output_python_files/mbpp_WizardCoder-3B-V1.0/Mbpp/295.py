"""
Write a function to return the sum of all divisors of a number.
assert sum_div(8)==7
"""

def sum_div(n):
    div = 1
    for i in range(1, n+1):
        if n % i == 0:
            div += i
    return div

print(sum_div(8))<|endoftext|>