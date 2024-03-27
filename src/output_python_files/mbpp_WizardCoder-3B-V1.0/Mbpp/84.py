"""
Write a function to find the nth number in the newman conway sequence.
assert sequence(10) == 6
"""

def sequence(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return sequence(n-1) + sequence(n-2)

print(sequence(10))<|endoftext|>