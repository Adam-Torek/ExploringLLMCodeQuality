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
    for i in range(n):
        for j in range(i+1, n):
            if numbers[i] != numbers[j]:
                count += 1
    return count

assert count_pairs([1,2,1],3) == 2
assert count_pairs([1,2,3],3) == 3
assert count_pairs([1,1,1],3) == 0
assert count_pairs([1,1,1,1],4) == 0
assert count_pairs([1,1,1,1,1],5) == 0
assert count_pairs([1,1,1,1,1,1],6) == 0
assert count_pairs([1,1,1,1,1,1,1],7) == 0
assert count_pairs([1,1,1,1,1,1,1,1],8) == 0
assert count_pairs([1,1,1,1,1,1,1,1,1],9) == 0
assert count_pairs([1,1,1,1,1,1,1,1,1,1],10) == 0
assert count_pairs([1,1,1,1,1,1,1,1,1,1,1],11) == 0
assert count_pairs([1,1,1,1,1,1,1,1,1,1,1,1],12) == 0
assert count_pairs([1,1,1,1,1,1,1,1,1,1,1,1,1],13) == 0
assert count_pairs([1,1,1,1,1,1,1,1,1,1,1,1,1,1],14) == 0
assert count_pairs([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],15) == 0
assert count_pairs([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],16) == 0
assert count_pairs([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],17) == 0
assert count_pairs([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],18) == 0
assert count_pairs([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],19) == 0
assert count_pairs([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],20) == 0
assert count_pairs([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],21) == 0
assert count_pairs([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],22) == 0
assert count_pairs([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1