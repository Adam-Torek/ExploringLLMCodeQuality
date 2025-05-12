"""
Write a python function to count the number of pairs whose xor value is odd.
assert find_Odd_Pair([5,4,7,2,1],5) == 6
"""
def find_Odd_Pair(arr, xor):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[i] ^ arr[j]) == xor:
                count += 1
    return count


# Test the function
arr = [5,4,7,2,1]
xor = 5
print(find_Odd_Pair(arr,xor))