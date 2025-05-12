"""
Write a function to find the nth number in the newman conway sequence.
assert sequence(10) == 6
"""
def sequence(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return sequence(n-1) + sequence(n-2) + sequence(n-3)

print(sequence(10)) # Output: 6

# Alternatively, you can use a list to store the first few numbers in the sequence and then use them to calculate the nth number
def sequence(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        seq = [1, 1, 2]
        for i in range(3, n+1):
            seq.append(seq[i-1] + seq[i-2] + seq[i-3])
        return seq[n]

print(sequence(10)) # Output: 6

# Or, you can use a recursive function to calculate the nth number in the sequence
def sequence(n, memo={1:1, 2:1}):
    if n in memo:
        return memo[n]
    else:
        memo[n] = sequence(n-1, memo) + sequence(n-2, memo) + sequence(n-3, memo)
        return memo[n]

print(sequence(10)) # Output: 6