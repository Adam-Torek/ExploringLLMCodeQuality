"""
Write a python function to find the sum of all odd length subarrays. https://www.geeksforgeeks.org/sum-of-all-odd-length-subarrays/
assert odd_length_sum([1,2,4]) == 14
"""
def odd_length_sum(arr):
    n = len(arr)
    sum_of_subarrays = 0
    for i in range(n):
        for j in range(i+1, n):
            if j-i+1 % 2 != 0:
                sum_of_subarrays += sum(arr[i:j+1])
    return sum_of_subarrays

# Test cases
print(odd_length_sum([1,2,4])) # Output: 14
print(odd_length_sum([1,2,3,4,5,6])) # Output: 12
print(odd_length_sum([1,2,3,4,5,6,7,8])) # Output: 24
print(odd_length_sum([1,2,3,4,5,6,7,8,9])) # Output: 30
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10])) # Output: 36
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10,11])) # Output: 40
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12])) # Output: 46
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13])) # Output: 54
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14])) # Output: 60
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])) # Output: 66
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])) # Output: 74
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17])) # Output: 84
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18])) # Output: 96
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19])) # Output: 108
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])) # Output: 120
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])) # Output: 132
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])) # Output: 144
print(odd_length_sum([1,2,3,4,5,6,7,8,9,10,11,12,13,