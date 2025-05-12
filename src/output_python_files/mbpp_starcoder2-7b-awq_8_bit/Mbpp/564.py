"""
Write a python function which takes a list of integers and counts the number of possible unordered pairs where both elements are unequal.
assert count_Pairs([1,2,1],3) == 2
"""

def count_Pairs(lst, n):
    count = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i]!= lst[j]:
                count += 1
    return count

assert count_Pairs([1,2,1],3) == 2
assert count_Pairs([1,2,3],3) == 3
assert count_Pairs([1,2,3,4],4) == 6
assert count_Pairs([1,2,3,4,5],5) == 10
assert count_Pairs([1,2,3,4,5,6],6) == 15
assert count_Pairs([1,2,3,4,5,6,7],7) == 21
assert count_Pairs([1,2,3,4,5,6,7,8],8) == 28
assert count_Pairs([1,2,3,4,5,6,7,8,9],9) == 36
assert count_Pairs([1,2,3,4,5,6,7,8,9,10],10) == 45
assert count_Pairs([1,2,3,4,5,6,7,8,9,10,11],11) == 55
assert count_Pairs([1,2,3,4,5,6,7,8,9,10,11,12],12) == 66
assert count_Pairs([1,2,3,4,5,6,7,8,9,10,11,12,13],13) == 78
assert count_Pairs([1,2,3,4,5,6,7,8,9,10,11,12,13,14],14) == 91
assert count_Pairs([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],15) == 105
assert count_Pairs([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],16) == 120
assert count_Pairs([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],17) == 136
assert count_Pairs([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18],18) == 153
assert count_Pairs([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],19) == 171
assert count_Pairs([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],20) == 190
assert count_Pairs([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21],21) == 210
assert count_Pairs([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22],22) == 231
assert count_Pairs([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,