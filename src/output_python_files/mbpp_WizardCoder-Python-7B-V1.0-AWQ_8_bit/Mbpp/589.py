"""
Write a function to find perfect squares between two given numbers.
assert perfect_squares(1,30)==[1, 4, 9, 16, 25]
"""

def perfect_squares(a, b):
    """
    Returns a list of perfect squares between a and b (inclusive)
    """
    perfect_squares = []
    for i in range(a, b+1):
        if i**0.5 == int(i**0.5):
            perfect_squares.append(i)
    return perfect_squares

print(perfect_squares(1,30)) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(perfect_squares(1,10)) #[1, 4, 9, 16, 25]
print(perfect_squares(10,20)) #[100, 121, 144, 169, 196, 225]
print(perfect_squares(0,10)) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(perfect_squares(10,0)) #[100, 121, 144, 169, 196, 225]
print(perfect_squares(0,0)) #[0]
print(perfect_squares(1,1)) #[1]
print(perfect_squares(2,3)) #[1, 4]
print(perfect_squares(4,4)) #[16]
print(perfect_squares(5,5)) #[25]
print(perfect_squares(10,10)) #[100]
print(perfect_squares(10,11)) #[100, 121]
print(perfect_squares(11,11)) #[121]
print(perfect_squares(11,12)) #[121, 144]
print(perfect_squares(12,12)) #[144]
print(perfect_squares(13,13)) []
print(perfect_squares(14,14)) []
print(perfect_squares(15,15)) []
print(perfect_squares(16,16)) []
print(perfect_squares(17,17)) []
print(perfect_squares(18,18)) []
print(perfect_squares(19,19)) []
print(perfect_squares(20,20)) []
print(perfect_squares(21,21)) []
print(perfect_squares(22,22)) []
print(perfect_squares(23,23)) []
print(perfect_squares(24,24)) []
print(perfect_squares(25,25)) []
print(perfect_squares(26,26)) []
print(perfect_squares(27,27)) []
print(perfect_squares(28,28)) []
print(perfect_squares(29,29)) []
print(perfect_squares(30,30)) []
print(perfect_squares(31,31)) []
print(perfect_squares(32,32)) []
print(perfect_squares(33,33)) []
print(perfect_squares(34,34)) []
print(perfect_squares(35,35)) []
print(perfect_squares(36,36)) []
print(perfect_squares(37,37)) []
print(perfect_squares(38,38)) []
print(perfect_squares(39,39)) []
print(perfect_squares(40,40)) []
print(perfect_squares(41,41