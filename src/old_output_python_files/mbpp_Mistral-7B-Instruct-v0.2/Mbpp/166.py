"""
Write a function that counts the number of pairs of integers in a list that xor to an even number.
assert find_even_pair([5, 4, 7, 2, 1]) == 4
"""
def find_even_pair(numbers):
    count = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if (numbers[i] ^ numbers[j]) % 2 == 0:
                count += 1
                break
    return count

assert find_even_pair([5, 4, 7, 2, 1]) == 4
assert find_even_pair([1, 2, 3, 4, 5]) == 2
assert find_even_pair([1, 1, 1, 1, 1]) == 0
assert find_even_pair([1, 1, 1, 1, 2]) == 1
assert find_even_pair([1, 1, 1, 1, 3]) == 0
assert find_even_pair([1, 1, 1, 1, 4]) == 1
assert find_even_pair([1, 1, 1, 1, 5]) == 0
assert find_even_pair([1, 1, 1, 1, 6]) == 1
assert find_even_pair([1, 1, 1, 1, 7]) == 0
assert find_even_pair([1, 1, 1, 1, 8]) == 1
assert find_even_pair([1, 1, 1, 1, 9]) == 0
assert find_even_pair([1, 1, 1, 1, 10]) == 1
assert find_even_pair([1, 1, 1, 1, 11]) == 0
assert find_even_pair([1, 1, 1, 1, 12]) == 1
assert find_even_pair([1, 1, 1, 1, 13]) == 0
assert find_even_pair([1, 1, 1, 1, 14]) == 1
assert find_even_pair([1, 1, 1, 1, 15]) == 0
assert find_even_pair([1, 1, 1, 1, 16]) == 1
assert find_even_pair([1, 1, 1, 1, 17]) == 0
assert find_even_pair([1, 1, 1, 1, 18]) == 1
assert find_even_pair([1, 1, 1, 1, 19]) == 0
assert find_even_pair([1, 1, 1, 1, 20]) == 1
assert find_even_pair([1, 1, 1, 1, 21]) == 0
assert find_even_pair([1, 1, 1, 1, 22]) == 1
assert find_even_pair([1, 1, 1, 1, 23]) == 0
assert find_even_pair([1, 1, 1, 1, 24]) == 1
assert find_even_pair([1, 1, 1, 1, 25]) == 0
assert find_even_pair([1, 1, 1, 1, 26]) == 1
assert find_even_pair([1, 1, 1, 1, 27]) == 0
assert find_even_pair([1, 1, 1, 1, 28]) == 1
assert find_even_pair([1, 1, 1, 1, 29]) == 0
assert find_even_pair([1, 1, 1, 1, 30]) == 1
assert find_even_pair([1, 1, 1, 1, 31]) == 0
assert find_even_pair([1, 1, 1, 1, 32]) == 1
assert find_even_pair([1, 1, 1,