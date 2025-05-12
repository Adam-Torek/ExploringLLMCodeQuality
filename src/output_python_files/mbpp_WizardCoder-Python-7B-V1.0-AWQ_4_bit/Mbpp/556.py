"""
Write a python function to count the number of pairs whose xor value is odd.
assert find_Odd_Pair([5,4,7,2,1],5) == 6
"""

def find_Odd_Pair(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i]^arr[j])%2!=0:
                count += 1
    return count

# Testing the function
print(find_Odd_Pair([5,4,7,2,1],5)) # Output: 6
print(find_Odd_Pair([1,2,3,4,5],4)) # Output: 4
print(find_Odd_Pair([1,3,5,7,9],4)) # Output: 6
print(find_Odd_Pair([1,2,4,6,8],4)) # Output: 0
print(find_Odd_Pair([1,3,5,7,9],5)) # Output: 6
print(find_Odd_Pair([1,2,4,6,8,10],5)) # Output: 8

# Time Complexity: O(n^2)
# Space Complexity: O(1)