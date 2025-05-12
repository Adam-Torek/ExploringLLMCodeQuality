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

print(get_pairs_count([1,1,1,1],2)) # Output: 6
print(get_pairs_count([1,2,3,4,5],9)) # Output: 2
print(get_pairs_count([1,2,3,4,5],10)) # Output: 4
print(get_pairs_count([1,2,3,4,5],0)) # Output: 0
print(get_pairs_count([1,2,3,4,5],1)) # Output: 0
print(get_pairs_count([1,2,3,4,5],6)) # Output: 2
print(get_pairs_count([1,2,3,4,5],7)) # Output: 3
print(get_pairs_count([1,2,3,4,5],8)) # Output: 4
print(get_pairs_count([1,2,3,4,5],11)) # Output: 0

# Time Complexity: O(n^2)
# Space Complexity: O(1)

# Improved version using dictionary
def get_pairs_count_dict(numbers, sum):
    count = 0
    d = {}
    for i in numbers:
        if sum - i in d:
            count += d[sum - i]
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return count

print(get_pairs_count_dict([1,1,1,1],2)) # Output: 6
print(get_pairs_count_dict([1,2,3,4,5],9)) # Output: 2
print(get_pairs_count_dict([1,2,3,4,5],10)) # Output: 4
print(get_pairs_count_dict([1,2,3,4,5],0)) # Output: 0
print(get_pairs_count_dict([1,2,3,4,5],1)) # Output: 0
print(get_pairs_count_dict([1,2,3,4,5],6)) # Output: 2
print(get_pairs_count_dict([1,2,3,4,5],7)) # Output: 3
print(get_pairs_count_dict([1,2,3,4,5],8)) # Output: 4
print(get_pairs_count_dict([1,2,3,4,5],11)) # Output: 0

# Time Complexity: O(n)
# Space Complexity: O(n)

# Using set
def get_pairs_count_set(numbers, sum):
    count = 0
    s = set()
    for i in numbers:
        if sum - i in s:
            count += 1
        s.add(i)
    return count

print(get_pairs_count_set([1,1,1,1],2)) # Output: 6
print(get_pairs_count_set([1,2,3,4,5],9)) # Output: 2
print(get_pairs_count_set([1,2,3,4,5],10)) # Output: 4
print(get_pairs_count_set([1,2,3,4,5],0)) # Output: 0
print(get_pairs_count_set([1,2,3,4,5],1)) # Output: 0
print(get_pairs_count