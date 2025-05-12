"""
Write a python function which takes a list of integers and counts the number of possible unordered pairs where both elements are unequal.
assert count_Pairs([1,2,1],3) == 2
"""

def count_Pairs(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] != arr[j]:
                count += 1
    return count


if __name__ == '__main__':
    print(count_Pairs([1,2,1],3))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],10))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],11))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],12))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],13))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],14))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],15))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],16))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],17))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],18))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],19))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],20))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],21))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],22))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],23))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],24))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],25))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],26))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],27))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],28))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],29))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],30))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],31))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],32))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],33))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],34))
    print(count_Pairs([1,2,3,4,5,6,7,8,9,10],35))
    print(count_Pairs([1,2,3,4,5,6,7,8