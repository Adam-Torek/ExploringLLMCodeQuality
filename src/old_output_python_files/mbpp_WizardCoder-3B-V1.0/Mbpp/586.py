"""
Write a python function to split a list at the nth eelment and add the first part to the end.
assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
"""
def split_Arr(arr, n):
    if n == 1:
        return arr
    else:
        return split_Arr(arr[n:], n-1) + [arr[0]]

# Test the function
print(split_Arr([12,10,5,6,52,36],2))<|endoftext|>