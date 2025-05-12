"""
Write a python function to find the largest number that can be formed with the given list of digits.
assert find_Max_Num([1,2,3]) == 321
"""

def find_Max_Num(digits):
    return int(''.join(sorted(digits, reverse=True)))

print(find_Max_Num([1,2,3]))
/python/leetcode/easy/1410_HTML_entity_parser.py
"""
Given a string representing an HTML session, you need to return a string representing the HTML session after decoding all the entities.

The valid entity characters are:

'(', ')', '&', ';', '!', '<', '>', and '"'

assert decode_html("&amp; is an entity&amp;") == "& is an entity&"
"""

def decode_html(text):
    return text.replace("&amp;", "&").replace("&gt;", ">").replace("&lt;", "<").replace("&quot;", "\"").replace("&#39;", "'")

print(decode_html("&amp; is an entity&amp;"))
/python/leetcode/easy/1365_how_many_numbers_are_smaller_than_the_current_number.py
"""
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, the number of valid pairs (i, j) where i < j and nums[i] < nums[j]

assert smaller_numbers_than_current([8,1,2,2,3]) == [4,0,1,1,3]
"""

def smaller_numbers_than_current(nums):
    return [sum(num < n for num in nums) for n in nums]

print(smaller_numbers_than_current([8,1,2,2,3]))
/python/leetcode/easy/1431_kids_with_the_greatest_number_of_candies.py
"""
Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.

assert kids_with_candies([2,3,5,1,3], 3) == [true, true, true, false, true]
"""

def kids_with_candies(candies, extraCandies):
    max_candies = max(candies)
    return [candy + extraCandies >= max_candies for candy in candies]

print(kids_with_candies([2,3,5,1,3], 3))
/python/leetcode/easy/1470_shuffle_the_array.py
"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

assert shuffle([2,5,1,3,4,7], 3) == [2,3,5,4,1,7]
"""

def shuffle(nums, n):
    return [nums[i] for i in range(n)] + [nums[i + n] for i in range(n)]

print(shuffle([2,5,1,3,4,7], 3))
/python/leetcode/easy/1389_create_target_array_in_the_given_order.py
"""
Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

assert create_target_array([0,1,2,3,4], [0,1,2,2,1]) == [0,4,1,3,2]
"""

def create_target_array(nums, index):
    target = []
    for i in range(len(nums)):