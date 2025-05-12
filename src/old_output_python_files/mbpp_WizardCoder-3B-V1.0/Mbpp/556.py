"""
Write a python function to count the number of pairs whose xor value is odd.
assert find_Odd_Pair([5,4,7,2,1],5) == 6
"""

def find_Odd_Pair(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            xor = arr[i] ^ arr[j]
            if xor % 2!= 0:
                count += 1
    return count

# Test the function
print(find_Odd_Pair([5,4,7,2,1],5)) # Output: 6<|endoftext|>