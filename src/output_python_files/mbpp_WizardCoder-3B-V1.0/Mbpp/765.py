"""
Write a function to find nth polite number. geeksforgeeks.org/n-th-polite-number/
assert is_polite(7) == 11
"""
def is_polite(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    elif n == 4:
        return 5
    elif n == 5:
        return 8
    elif n == 6:
        return 13
    elif n == 7:
        return 21
    elif n == 8:
        return 34
    elif n == 9:
        return 55
    elif n == 10:
        return 89
    elif n == 11:
        return 144
    elif n == 12:
        return 233
    elif n == 13:
        return 377
    elif n == 14:
        return 610
    elif n == 15:
        return 987
    elif n == 16:
        return 1597
    elif n == 17:
        return 2584
    elif n == 18:
        return 4181
    elif n == 19:
        return 6765
    elif n == 20:
        return 10946
    elif n == 21:
        return 17711
    elif n == 22:
        return 28657
    elif n == 23:
        return 46368
    elif n == 24:
        return 75025
    elif n == 25:
        return 121393
    elif n == 26:
        return 196418
    elif n == 27:
        return 317811
    elif n == 28:
        return 514229
    elif n == 29:
        return 832040
    elif n == 30:
        return 1346269
    elif n == 31:
        return 2178309
    elif n == 32:
        return 3524578
    elif n == 33:
        return 5702887
    elif n == 34:
        return 9227465
    elif n == 35:
        return 14930352
    elif n == 36:
        return 24157817
    elif n == 37:
        return 39088169
    elif n == 38:
        return 63245986
    elif n == 39:
        return 102334155
    elif n == 40:
        return 165580141
    elif n == 41:
        return 267914296
    elif n == 42:
        return 433494437
    elif n == 43:
        return 701408733
    elif n == 44:
        return 1134903170
    elif n == 45:
        return 1836311903
    elif n == 46:
        return 2971215073
    elif n == 47:
        return 4807526976
    elif n == 48:
        return 7778742049
    elif n == 49:
        return 12586269025
    elif n == 50:
        return 20365011074
    elif n == 51:
        return 32951280099
    elif n == 52:
        return 53316291173
    elif n == 53:
        return 86267571272
    elif n == 54:
        return 139583862445
    elif n == 55:
        return 225851433717
    elif n == 56:
        return 365435296162
    elif n == 57:
        return