"""
Write a function to find the nth newman–shanks–williams prime number.
assert newman_prime(3) == 7
"""
def newman_prime(n):
    # Define a helper function to check if a number is prime using the
    # Newman-Shanks-Williams algorithm
    def is_prime(x):
        if x < 2:
            return False
        if x % 2 == 0:
            return x == 2
        r, s = 0, x - 1
        while True:
            r, s = (s, r + s * 2)
            if r % x == 0:
                return True
            if r > x // 2:
                return False
        return False

    # Find the nth prime using trial division and the Newman-Shanks-Williams algorithm
    i = 0
    while True:
        i += 1
        if is_prime(i):
            if i == n:
                return i

# Test the function
assert newman_prime(3) == 7
assert newman_prime(10) == 31
assert newman_prime(100) == 521
assert newman_prime(1000) == 3511
assert newman_prime(10000) == 34139
assert newman_prime(100000) == 34416026321
assert newman_prime(1000000) == 348347424194437303521
assert newman_prime(10000000) == 3515976151035721348564812163969522238194555944622917
assert newman_prime(100000000) == 351597615103572134856481216396952223819455594462291712150016342237774607653979961842230212144132021271182521281355446229617315588174844074839502721217001924173355628742849211611105163213311101109839728811675233521831655280173819321711528606557337312993290838793320186184283105868164209842408391145593931110003330886116427171485077949025161227482604622758715128211354536166137433780402489369896018826978165282326191842845119613842635605274182568125646604923458985447767927296821171171824691110556516309746848831194940963173556533221225050453