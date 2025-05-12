"""
Write a function to sum the length of the names of a given list of names after removing the names that start with a lowercase letter.
assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
"""

def sample_nam(names):
    total_length = 0
    for name in names:
        if name[0].isupper():
            total_length += len(name)
    return total_length

print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])) # Output: 16
print(sample_nam(['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'])) # Output: 0
print(sample_nam(['A', 'b', 'C', 'd', 'E'])) # Output: 0
print(sample_nam(['A', 'B', 'C', 'D', 'E'])) # Output: 0
print(sample_nam(['a', 'b', 'c', 'd', 'e'])) # Output: 0
print(sample_nam([''])) # Output: 0
print(sample_nam([])) # Output: 0
print(sample_nam(['a'])) # Output: 0
print(sample_nam(['A'])) # Output: 1
print(sample_nam(['a', 'A', 'b', 'B', 'c', 'C'])) # Output: 0
print(sample_nam(['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E'])) # Output: 0
print(sample_nam(['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F'])) # Output: 0
print(sample_nam(['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G'])) # Output: 0
print(sample_nam(['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H'])) # Output: 0
print(sample_nam(['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I'])) # Output: 0
print(sample_nam(['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J'])) # Output: 0
print(sample_nam(['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K'])) # Output: 0
print(sample_nam(['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L'])) # Output: 0
print(sample_nam(['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M'])) # Output: 0
print(sample_nam(['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N']))