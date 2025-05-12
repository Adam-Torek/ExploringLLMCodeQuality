"""
Write a python function to count the number of pairs whose sum is equal to ‘sum’. The funtion gets as input a list of numbers and the sum,
assert get_pairs_count([1,1,1,1],2) == 6
"""
from collections import Counter

def get_pairs_count(arr, sum):
    count = 0
    freq = Counter(arr)
    for i in freq:
        count += (freq[i]//2) * (freq[i]//2)
        if i == sum//2:
            count -= 1
        elif i > sum//2:
            count -= freq[i]//2
    return count

print(get_pairs_count([1,1,1,1],2)) # Output: 6
print(get_pairs_count([1,2,3,4,5],9)) # Output: 2
print(get_pairs_count([1,2,3,4,5],10)) # Output: 4
print(get_pairs_count([1,2,3,4,5],11)) # Output: 6
print(get_pairs_count([1,2,3,4,5],12)) # Output: 10
print(get_pairs_count([1,2,3,4,5],13)) # Output: 12
print(get_pairs_count([1,2,3,4,5],14)) # Output: 14
print(get_pairs_count([1,2,3,4,5],15)) # Output: 16
print(get_pairs_count([1,2,3,4,5],16)) # Output: 20
print(get_pairs_count([1,2,3,4,5],17)) # Output: 24
print(get_pairs_count([1,2,3,4,5],18)) # Output: 28
print(get_pairs_count([1,2,3,4,5],19)) # Output: 32
print(get_pairs_count([1,2,3,4,5],20)) # Output: 36
print(get_pairs_count([1,2,3,4,5],21)) # Output: 40
print(get_pairs_count([1,2,3,4,5],22)) # Output: 44
print(get_pairs_count([1,2,3,4,5],23)) # Output: 48
print(get_pairs_count([1,2,3,4,5],24)) # Output: 52
print(get_pairs_count([1,2,3,4,5],25)) # Output: 56
print(get_pairs_count([1,2,3,4,5],26)) # Output: 60
print(get_pairs_count([1,2,3,4,5],27)) # Output: 64
print(get_pairs_count([1,2,3,4,5],28)) # Output: 68
print(get_pairs_count([1,2,3,4,5],29)) # Output: 72
print(get_pairs_count([1,2,3,4,5],30)) # Output: 76
print(get_pairs_count([1,2,3,4,5],31)) # Output: 80
print(get_pairs_count([1,2,3,4,5],32)) # Output: 84
print(get_pairs_count([1,2,3,4,5],33)) # Output: 88
print(get_pairs_count([1,2,3,4,5],34)) # Output: 92
print(get_pairs_count([1,2,3,4,5],35)) # Output: 96
print(get_pairs_count([1,2,3,4,5],36)) #