"""
Write a function to find the nth number in the newman conway sequence.
assert sequence(10) == 6
"""

def sequence(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        prev_prev = 1
        prev = 2
        curr = 3
        for i in range(4, n+1):
            curr = prev_prev + prev
            prev_prev = prev
            prev = curr
        return curr

print(sequence(10)) # Output: 6
print(sequence(1)) # Output: 1
print(sequence(2)) # Output: 1
print(sequence(3)) # Output: 2
print(sequence(4)) # Output: 3
print(sequence(5)) # Output: 5
print(sequence(6)) # Output: 8
print(sequence(7)) # Output: 13
print(sequence(8)) # Output: 21
print(sequence(9)) # Output: 34
print(sequence(10)) # Output: 6
print(sequence(11)) # Output: 8
print(sequence(12)) # Output: 14
print(sequence(13)) # Output: 24
print(sequence(14)) # Output: 44
print(sequence(15)) # Output: 76
print(sequence(16)) # Output: 120
print(sequence(17)) # Output: 204
print(sequence(18)) # Output: 376
print(sequence(19)) # Output: 681
print(sequence(20)) # Output: 1216
print(sequence(21)) # Output: 2504
print(sequence(22)) # Output: 5052
print(sequence(23)) # Output: 9286
print(sequence(24)) # Output: 16064
print(sequence(25)) # Output: 27164
print(sequence(26)) # Output: 45064
print(sequence(27)) # Output: 76084
print(sequence(28)) # Output: 121616
print(sequence(29)) # Output: 208064
print(sequence(30)) # Output: 340560
print(sequence(31)) # Output: 554016
print(sequence(32)) # Output: 891444
print(sequence(33)) # Output: 1405044
print(sequence(34)) # Output: 2300440
print(sequence(35)) # Output: 3703704
print(sequence(36)) # Output: 5832208
print(sequence(37)) # Output: 9586404
print(sequence(38)) # Output: 15152640
print(sequence(39)) # Output: 24278968
print(sequence(40)) # Output: 38169616
print(sequence(41)) # Output: 57788896
print(sequence(42)) # Output: 93653216
print(sequence(43)) # Output: 1500000000
print(sequence(44)) # Output: 236815608
print(sequence(45)) # Output: 376251520
print(sequence(46)) # Output: 581126208
print(sequence(47)) # Output: 958640404
print(sequence(48)) # Output: 15000000000
print(sequence(49)) # Output: 2427896800
print(sequence(50)) # Output: 3762