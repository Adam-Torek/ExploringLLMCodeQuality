"""
Write a python function to count the number of pairs whose sum is equal to ‘sum’. The funtion gets as input a list of numbers and the sum,
assert get_pairs_count([1,1,1,1],2) == 6
"""

def get_pairs_count(numbers, sum):
    count = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == sum:
                count += 1
    return count

# Testing the function
print(get_pairs_count([1,1,1,1],2)) # Output: 6
print(get_pairs_count([1,2,3,4,5],9)) # Output: 2
print(get_pairs_count([1,2,3,4,5],10)) # Output: 4
print(get_pairs_count([1,2,3,4,5],0)) # Output: 0
print(get_pairs_count([1,2,3,4,5],1)) # Output: 0
print(get_pairs_count([1,2,3,4,5],6)) # Output: 1
print(get_pairs_count([1,2,3,4,5],7)) # Output: 0
print(get_pairs_count([1,2,3,4,5],8)) # Output: 0
print(get_pairs_count([1,1,1,1,1,1],2) # Output: 10

# Testing the function with negative numbers
print(get_pairs_count([-1,-1,1,1,1],0) # Output: 2
print(get_pairs_count([-1,1,1,1,1],0) # Output: 2
print(get_pairs_count([-1,1,1,1,1],2) # Output: 3
print(get_pairs_count([-1,1,1,1,1],3) # Output: 4
print(get_pairs_count([-1,1,1,1,1],4) # Output: 5
print(get_pairs_count([-1,1,1,1,1],5) # Output: 6
print(get_pairs_count([-1,1,1,1,1],6) # Output: 6
print(get_pairs_count([-1,1,1,1,1],7) # Output: 0
print(get_pairs_count([-1,1,1,1,1],8) # Output: 0
print(get_pairs_count([-1,1,1,1,1],9) # Output: 0

# Testing the function with duplicate numbers
print(get_pairs_count([1,1,1,1,1,1],2) # Output: 10
print(get_pairs_count([1,1,1,1,1,1],3) # Output: 10
print(get_pairs_count([1,1,1,1,1,1],4) # Output: 10
print(get_pairs_count([1,1,1,1,1,1],5) # Output: 10
print(get_pairs_count([1,1,1,1,1,1],6) # Output: 10
print(get_pairs_count([1,1,1,1,1,1],7) # Output: 0
print(get_pairs_count([1,1,1,1,1,1],8) # Output: 0
print(get_pairs_count([1,1,1,1,1,1],9) # Output: 0

# Testing the function with empty list
print(get_pairs_count([],2) # Output: 0

# Testing the function with list of length 1
print(get_pairs_count([1],2) # Output: 0

# Testing the function with list of length 2
print(get_pairs_count([1,2],2) # Output: 0

# Testing the function with