"""
Write a python function to count the number of pairs whose xor value is odd.
assert find_Odd_Pair([5,4,7,2,1],5) == 6
"""
def find_Odd_Pair(arr, n):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i]^arr[j])%2!=0:
                count+=1
    return count

# Test the function
assert find_Odd_Pair([5,4,7,2,1],5) == 6
assert find_Odd_Pair([1,2,3,4,5],4) == 4
assert find_Odd_Pair([1,3,5,7,9],4) == 4
assert find_Odd_Pair([1,2,4,6,8],4) == 0
assert find_Odd_Pair([1,3,5,7,9],5) == 6
assert find_Odd_Pair([1,2,4,6,8,10],5) == 5
assert find_Odd_Pair([1,2,3,4,5,6,7,8,9,10],8) == 10
assert find_Odd_Pair([1,3,5,7,9,11],5) == 6
assert find_Odd_Pair([1,2,4,6,8,10,12],6) == 6
assert find_Odd_Pair([1,3,5,7,9,11,13],6) == 6
assert find_Odd_Pair([1,2,4,6,8,10,12,14],6) == 6
assert find_Odd_Pair([1,3,5,7,9,11,13,15],6) == 6
assert find_Odd_Pair([1,2,4,6,8,10,12,14,16],7) == 7
assert find_Odd_Pair([1,3,5,7,9,11,13,15,17],7) == 7
assert find_Odd_Pair([1,2,4,6,8,10,12,14,16,18],7) == 7
assert find_Odd_Pair([1,3,5,7,9,11,13,15,17,19],7) == 7
assert find_Odd_Pair([1,2,4,6,8,10,12,14,16,18,20],8) == 8
assert find_Odd_Pair([1,3,5,7,9,11,13,15,17,19,21],8) == 8
assert find_Odd_Pair([1,2,4,6,8,10,12,14,16,18,20,22],8) == 8
assert find_Odd_Pair([1,3,5,7,9,11,13,15,17,19,21,23],8) == 8
assert find_Odd_Pair([1,2,4,6,8,10,12,14,16,18,20,22,24],9) == 9
assert find_Odd_Pair([1,3,5,7,9,11,13,15,17,19,21,23,25],9) == 9
assert find_Odd_Pair([1,2,4,6,8,10,12,14,16,18,20,22,24,26],9) == 9
assert find_Odd_Pair([1,3,5,7,9,11,13,15,17,19,21,23,25,27],9) == 9
assert find_Odd_Pair([1,2,4,6,8,10,12,1