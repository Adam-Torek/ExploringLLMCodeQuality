"""
Write a function that counts the number of pairs of integers in a list that xor to an even number.
assert find_even_pair([5, 4, 7, 2, 1]) == 4
"""
def find_even_pair(numbers):
    count = 0
    for i in numbers:
        for j in numbers:
            if i != j and (i ^ j) % 2 == 0:
                count += 1
                break
    return count

assert find_even_pair([5, 4, 7, 2, 1]) == 4
assert find_even_pair([1, 2, 3, 4, 5]) == 2
assert find_even_pair([1, 1, 1, 1, 1]) == 0
assert find_even_pair([]) == 0
assert find_even_pair([1]) == 0
assert find_even_pair([1, 1]) == 0
assert find_even_pair([1, 1, 1, 1, 1, 1]) == 0
assert find_even_pair([1, 1, 1, 1, 1, 1, 1]) == 0
assert find_even_pair([1, 1, 1, 1, 1, 1, 1, 1]) == 0
assert find_even_pair([1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
assert find_even_pair([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
assert find_even_pair([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
assert find_even_pair([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
assert find_even_pair([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
assert find_even_pair([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
assert find_even_pair([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
assert find_even_pair([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
assert find_even_pair([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
assert find_even_pair([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
assert find_even_pair([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
assert find_even_pair([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 0
assert find_even_pair([1, 1, 1, 1, 1, 1, 1