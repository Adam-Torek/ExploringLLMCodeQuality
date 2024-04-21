"""
Write a function to check whether the given number is armstrong or not.
assert armstrong_number(153)==True
"""
def armstrong_number(num):
    num_str = str(num)
    num_len = len(num_str)
    sum_of_squares = 0
    for i in range(num_len):
        square = int(num_str[i]) ** num_len
        sum_of_squares += square
    return num == sum_of_squares

# Test cases
assert armstrong_number(153) == True
assert armstrong_number(123) == False
assert armstrong_number(100) == True
assert armstrong_number(10) == True
assert armstrong_number(9474) == True
assert armstrong_number(1531622510) == True<|endoftext|>