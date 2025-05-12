"""
Write a python function which takes a list of integers and counts the number of possible unordered pairs where both elements are unequal.
assert count_Pairs([1,2,1],3) == 2
"""
def count_pairs(numbers, n):
    """
    :param numbers: list of integers
    :param n: size of the list
    :return: number of possible unordered pairs where both elements are unequal
    """
    count = 0
    # create a set to store unique integers in the list
    unique_numbers = set(numbers)
    # iterate through the set and count the number of pairs for each unique integer
    for num in unique_numbers:
        count += numbers.count(num) - 1
    return count * (len(unique_numbers) - 1) // 2

assert count_pairs([1,2,1],3) == 2
assert count_pairs([1,2,3],3) == 3
assert count_pairs([1,1,1],3) == 0
assert count_pairs([1,1,1,1],4) == 0
assert count_pairs([1,2,3,4],5) == 6
assert count_pairs([1,2,3,4,5],6) == 10
assert count_pairs([1,2,3,4,5,6],7) == 15
assert count_pairs([1,2,3,4,5,6,7],8) == 21
assert count_pairs([1,2,3,4,5,6,7,8],9) == 28
assert count_pairs([1,2,3,4,5,6,7,8,9],10) == 36
assert count_pairs([1,2,3,4,5,6,7,8,9,10],11) == 45
assert count_pairs([1,2,3,4,5,6,7,8,9,10,11],12) == 55
assert count_pairs([1,2,3,4,5,6,7,8,9,10,11,12],13) == 66
assert count_pairs([1,2,3,4,5,6,7,8,9,10,11,12,13],14) == 78
assert count_pairs([1,2,3,4,5,6,7,8,9,10,11,12,13,14],15) == 91
assert count_pairs([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],16) == 106
assert count_pairs([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],17) == 123
assert count_pairs([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],18) == 142
assert count_pairs([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],19) == 163
assert count_pairs([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],20) == 186
assert count_pairs([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],21) == 212
assert count_pairs([1,2,3,4,5,6,7,8,9,10,11,12,13,14