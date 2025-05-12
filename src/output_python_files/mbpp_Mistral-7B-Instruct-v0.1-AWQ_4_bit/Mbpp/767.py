"""
Write a python function to count the number of pairs whose sum is equal to ‘sum’. The funtion gets as input a list of numbers and the sum,
assert get_pairs_count([1,1,1,1],2) == 6
"""

def get_pairs_count(numbers, sum):
    pairs = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == sum:
                pairs.append((numbers[i], numbers[j]))
    return len(pairs)

# test
print(get_pairs_count([1,1,1,1],2))