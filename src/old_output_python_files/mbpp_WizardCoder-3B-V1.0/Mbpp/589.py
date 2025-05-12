"""
Write a function to find perfect squares between two given numbers.
assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
"""

def perfect_squares(a, b):
    squares = []
    for i in range(a, b+1):
        if i**2 == i:
            squares.append(i)
    return squares

print(perfect_squares(1,30))<|endoftext|>