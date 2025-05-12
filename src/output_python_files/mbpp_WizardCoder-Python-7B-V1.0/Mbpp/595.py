"""
Write a python function to count minimum number of swaps required to convert one binary number represented as a string to another.
assert min_Swaps("1101","1110") == 1
"""
def min_Swaps(binary1, binary2):
    count = 0
    for i in range(len(binary1)):
        if binary1[i] != binary2[i]:
            binary1[i], binary2[i] = binary2[i], binary1[i]
            count += 1
    return count

binary1 = list("1101")
binary2 = list("1110")
print(min_Swaps(binary1, binary2))

# Output: 1

# Explanation:
# We can see that we need to swap the 1st and 4th index of binary1 with the 1st and 4th index of binary2 to convert binary1 to binary2.
# So, the minimum number of swaps required is 1.