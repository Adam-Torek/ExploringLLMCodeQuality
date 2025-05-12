"""
Write a function to find perfect squares between two given numbers.
assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
"""

def perfect_squares(a, b):
    """
    Returns a list of perfect squares between a and b (inclusive)
    """
    squares = []
    for i in range(a, b+1):
        if i**0.5 == int(i**0.5):
            squares.append(i)
    return squares

print(perfect_squares(1,30)) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(perfect_squares(1,10)) #[1, 4, 9, 16, 25]
print(perfect_squares(0,15)) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144]
print(perfect_squares(10,20)) #[100, 121, 144]
print(perfect_squares(0,0)) #[0]
print(perfect_squares(10,10)) #[10]
print(perfect_squares(10,11)) #[10, 11]
print(perfect_squares(10,12)) #[10, 11, 12]
print(perfect_squares(10,13)) #[10, 11, 12, 13]
print(perfect_squares(10,14)) #[10, 11, 12, 13, 14]
print(perfect_squares(10,15)) #[10, 11, 12, 13, 14, 15]
print(perfect_squares(10,16)) #[10, 11, 12, 13, 14, 15, 16]
print(perfect_squares(10,17)) #[10, 11, 12, 13, 14, 15, 16, 17]
print(perfect_squares(10,18)) #[10, 11, 12, 13, 14, 15, 16, 17, 18]
print(perfect_squares(10,19)) #[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(perfect_squares(10,20)) #[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(perfect_squares(10,21)) #[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25]
print(perfect_squares(10,22)) #[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26]
print(perfect_squares(10,23)) #[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26, 27]
print(perfect_squares(10,24)) #[10, 11, 12, 13, 14,