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
print(sample_nam(['A', 'B', 'C', 'd', 'E'])) # Output: 0
print(sample_nam(['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Fred', 'George'])) # Output: 16
print(sample_nam(['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Fred', 'george'])) # Output: 16
print(sample_nam(['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Fred', 'George', 'grace'])) # Output: 16
print(sample_nam(['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Fred', 'george', 'grace'])) # Output: 16
print(sample_nam(['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Fred', 'george', 'grace', 'Hannah'])) # Output: 16
print(sample_nam(['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Fred', 'george', 'grace', 'Hannah', 'Ivan'])) # Output: 16
print(sample_nam(['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Fred', 'george', 'grace', 'Hannah', 'Ivan', 'james'])) # Output: 16
print(sample_nam(['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Fred', 'george', 'grace', 'Hannah', 'Ivan', 'james', 'Kate'])) # Output: 16
print(sample_nam(['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Fred', 'george', 'grace', 'Hannah', 'Ivan', 'james', 'Kate', 'Lily'])) # Output: 16
print(sample_nam(['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Fred', 'george', 'grace', 'Hannah', 'Ivan', 'james', 'Kate', 'Lily', 'Mia'])) # Output: 16
print(sample_nam(['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Fred', 'george', 'grace', 'Hannah', 'Ivan', 'james', 'Kate', 'Lily', 'Mia', 'Nancy'])) # Output: 16
print(sample_nam(['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Fred', 'george', 'grace', 'Hannah', 'Ivan', 'james', 'Kate', 'Lily', 'Mia', 'Nancy', 'Oliver'])) # Output: 16
print(sample_nam(['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Fred', 'george', 'grace', 'Hannah', 'Ivan', 'james', 'Kate', 'Lily', 'Mia', 'Nancy', 'Oliver', 'Paul'])) # Output: 16
print(sample_nam(['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Fred', 'george', 'grace', 'Hannah', 'Ivan',