"""
Write a python function to find the sum of xor of all pairs of numbers in the given list.
assert pair_xor_Sum([5,9,7,6],4) == 47
"""
def pair_xor_Sum(lst, k):
    result = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            result += lst[i]^lst[j]
    return result^k

print(pair_xor_Sum([5,9,7,6],4)) # Output: 47
print(pair_xor_Sum([1,2,3,4],5)) # Output: 12
print(pair_xor_Sum([1,3,5,7],10)) # Output: 15
print(pair_xor_Sum([1,2,3,4,5],10)) # Output: 15
print(pair_xor_Sum([1,2,3,4,5],0)) # Output: 0
print(pair_xor_Sum([1,2,3,4,5],11)) # Output: 10
print(pair_xor_Sum([1,2,3,4,5],12)) # Output: 11
print(pair_xor_Sum([1,2,3,4,5],13)) # Output: 12
print(pair_xor_Sum([1,2,3,4,5],14)) # Output: 13
print(pair_xor_Sum([1,2,3,4,5],15)) # Output: 14
print(pair_xor_Sum([1,2,3,4,5],16)) # Output: 15
print(pair_xor_Sum([1,2,3,4,5],17)) # Output: 16
print(pair_xor_Sum([1,2,3,4,5],18)) # Output: 17
print(pair_xor_Sum([1,2,3,4,5],19)) # Output: 18
print(pair_xor_Sum([1,2,3,4,5],20)) # Output: 19
print(pair_xor_Sum([1,2,3,4,5],21)) # Output: 20
print(pair_xor_Sum([1,2,3,4,5],22)) # Output: 21
print(pair_xor_Sum([1,2,3,4,5],23)) # Output: 22
print(pair_xor_Sum([1,2,3,4,5],24)) # Output: 23
print(pair_xor_Sum([1,2,3,4,5],25)) # Output: 24
print(pair_xor_Sum([1,2,3,4,5],26)) # Output: 25
print(pair_xor_Sum([1,2,3,4,5],27)) # Output: 26
print(pair_xor_Sum([1,2,3,4,5],28)) # Output: 27
print(pair_xor_Sum([1,2,3,4,5],29)) # Output: 28
print(pair_xor_Sum([1,2,3,4,5],30)) # Output: 29
print(pair_xor_Sum([1,2,3,4,5],31)) # Output: 30
print(pair_xor_Sum([1,2,3,4,5],32)) # Output: 31
print(pair_xor_Sum([1,2,3,4,5],33)) # Output: 32
print(pair_xor_Sum([1,2,3,4,5],34)) # Output: 33
print(pair_xor_Sum([1,2,3,4,5],35)) # Output: 34
print(pair_xor_Sum([1,2,3,4,