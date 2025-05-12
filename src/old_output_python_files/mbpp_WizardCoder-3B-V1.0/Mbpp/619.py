"""
Write a function to move all the numbers to the end of the given string.
assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'
"""
def move_num(s):
    nums = []
    for i in s:
        if i.isdigit():
            nums.append(i)
    nums.sort(reverse=True)
    return ''.join(nums) + s[::-1]

assert move_num('I1love143you55three3000thousand') == 'Iloveyouthreethousand1143553000'<|endoftext|>