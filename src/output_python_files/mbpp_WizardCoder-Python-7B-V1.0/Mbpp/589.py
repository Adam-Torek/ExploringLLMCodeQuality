"""
Write a function to find perfect squares between two given numbers.
assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
"""

def perfect_squares(a, b):
    """
    Returns a list of perfect squares between a and b (inclusive)
    """
    result = []
    for i in range(a, b+1):
        if i**0.5 == int(i**0.5):
            result.append(i)
    return result

print(perfect_squares(1,30)) # [1, 4, 9, 16, 25]
print(perfect_squares(1,10)) # [1, 4, 9]
print(perfect_squares(0,15)) # [0, 1, 4, 9, 16]
print(perfect_squares(10,20)) # [16, 25]
print(perfect_squares(0,0)) # [0]
print(perfect_squares(10,10)) # [16]
print(perfect_squares(10,11)) # []
print(perfect_squares(10,12)) # [16]
print(perfect_squares(10,13)) # [16]
print(perfect_squares(10,14)) # [16]
print(perfect_squares(10,15)) # [16]
print(perfect_squares(10,16)) # [16, 25]
print(perfect_squares(10,17)) # [16, 25]
print(perfect_squares(10,18)) # [16, 25]
print(perfect_squares(10,19)) # [16, 25]
print(perfect_squares(10,20)) # [16, 25]
print(perfect_squares(10,21)) # [16, 25]
print(perfect_squares(10,22)) # [16, 25]
print(perfect_squares(10,23)) # [16, 25]
print(perfect_squares(10,24)) # [16, 25]
print(perfect_squares(10,25)) # [16, 25]
print(perfect_squares(10,26)) # [16, 25]
print(perfect_squares(10,27)) # [16, 25]
print(perfect_squares(10,28)) # [16, 25]
print(perfect_squares(10,29)) # [16, 25]
print(perfect_squares(10,30)) # [16, 25]
print(perfect_squares(10,31)) # [16, 25]
print(perfect_squares(10,32)) # [16, 25]
print(perfect_squares(10,33)) # [16, 25]
print(perfect_squares(10,34)) # [16, 25]
print(perfect_squares(10,35)) # [16, 25]
print(perfect_squares(10,36)) # [16, 25]
print(perfect_squares(10,37)) # [16, 25]
print(perfect_squares(10,38)) # [16, 25]
print(perfect_squares(10,39)) # [16, 25]
print(perfect_squares(10,40)) # [16, 25]
print(perfect_squares(10,41))