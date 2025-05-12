"""
Write a function to check whether the given number is armstrong or not.
assert armstrong_number(153)==True
"""
def armstrong_number(n):
    sum = 0
    n_str = str(n)
    for i in n_str:
        sum += int(i) ** len(n_str)
    return sum == n


# assert armstrong_number(153)==True
# assert armstrong_number(154)==False