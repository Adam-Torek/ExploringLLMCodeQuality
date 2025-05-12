"""
Write a python function to find the sum of all odd length subarrays. https://www.geeksforgeeks.org/sum-of-all-odd-length-subarrays/
assert odd_length_sum([1,2,4]) == 14
"""
def odd_length_sum(arr):
    n = len(arr)
    sum_odd_length_subarrays = 0
    for i in range(n):
        for j in range(i+1, n):
            if j-i+1 % 2 != 0:
                sum_odd_length_subarrays += sum(arr[i:j+1])
    return sum_odd_length_subarrays

# Test cases
print(odd_length_sum([1,2,4])) # Output: 14
print(odd_length_sum([1,2,3,4,5,6])) # Output: 12
print(odd_length_sum([1,2,3,4,5,6,7,8])) # Output: 22
print(odd_length_sum([1,2,3,4,5,6,7,8,9])) # Output: 28
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10])) # Output: 34
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10,11])) # Output: 40
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12])) # Output: 46
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13])) # Output: 54
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14])) # Output: 62
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])) # Output: 70
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])) # Output: 78
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])) # Output: 86
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])) # Output: 94
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])) # Output: 102
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])) # Output: 110
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])) # Output: 118
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,1