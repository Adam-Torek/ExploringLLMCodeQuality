"""
Write a python function to count the number of pairs whose xor value is odd.
assert find_Odd_Pair([5,4,7,2,1],5) == 6
"""
def find_Odd_Pair(arr, n):
    # XOR of all elements in array
    xor = 0
    for i in arr:
        xor ^= i

    # Find the bit which is set only once
    # in the binary representation of xor
    for i in range(32):
        if (xor & (1 << i)):
            bit = 1 << i
            count = 0
            for j in arr:
                if (bit & j):
                    count += 1
            if count % 2 != 0:
                return n - count

    return 0

arr = [5,4,7,2,1]
n = len(arr)
print(find_Odd_Pair(arr, n))</s>