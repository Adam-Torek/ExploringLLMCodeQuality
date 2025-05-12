"""
Write a python function to find the sum of xor of all pairs of numbers in the given list.
assert pair_xor_Sum([5,9,7,6],4) == 47
"""

def pair_xor_Sum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: int
    """
    result = 0
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            xor = numbers[i] ^ numbers[j]
            if xor == target:
                result += 1
    return result


#assert pair_xor_Sum([5,9,7,6],4) == 47
#assert pair_xor_Sum([1,2,3,4],1) == 10
#assert pair_xor_Sum([1,2,3,4],2) == 0
#assert pair_xor_Sum([1,2,3,4],3) == 1
#assert pair_xor_Sum([1,2,3,4],4) == 0
#assert pair_xor_Sum([1,2,3,4],5) == 1
#assert pair_xor_Sum([1,2,3,4],6) == 0
#assert pair_xor_Sum([1,2,3,4],7) == 1
#assert pair_xor_Sum([1,2,3,4],8) == 0
#assert pair_xor_Sum([1,2,3,4],9) == 1
#assert pair_xor_Sum([1,2,3,4],10) == 0
#assert pair_xor_Sum([1,2,3,4],11) == 1
#assert pair_xor_Sum([1,2,3,4],12) == 0
#assert pair_xor_Sum([1,2,3,4],13) == 1
#assert pair_xor_Sum([1,2,3,4],14) == 0
#assert pair_xor_Sum([1,2,3,4],15) == 1
#assert pair_xor_Sum([1,2,3,4],16) == 0
#assert pair_xor_Sum([1,2,3,4],17) == 1
#assert pair_xor_Sum([1,2,3,4],18) == 0
#assert pair_xor_Sum([1,2,3,4],19) == 1
#assert pair_xor_Sum([1,2,3,4],20) == 0
#assert pair_xor_Sum([1,2,3,4],21) == 1
#assert pair_xor_Sum([1,2,3,4],22) == 0
#assert pair_xor_Sum([1,2,3,4],23) == 1
#assert pair_xor_Sum([1,2,3,4],24) == 0
#assert pair_xor_Sum([1,2,3,4],25) == 1
#assert pair_xor_Sum([1,2,3,4],26) == 0
#assert pair_xor_Sum([1,2,3,4],27) == 1
#assert pair_xor_Sum([1,2,3,4],28) == 0
#assert pair_xor_Sum([1,2,3,4],29) == 1
#assert pair_xor_Sum([1,2,3,4],30) == 0
#assert pair_xor_Sum([1,2,3,4],31) == 1
#assert pair_xor_Sum([1,2,3,4],32) == 0
#assert pair_xor_Sum([1,2,3,4],33) == 1
#assert pair_xor_Sum([1,2,3,4],34) ==