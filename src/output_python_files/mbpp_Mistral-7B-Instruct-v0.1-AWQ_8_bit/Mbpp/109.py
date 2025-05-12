"""
Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.
assert odd_Equivalent("011001",6) == 3
"""

def odd_Equivalent(s,r):
    """
    :param s: string
    :param r: int
    :return: int
    """
    if r == 0:
        return 0
    else:
        return sum(1 for i in range(len(s)) if int(s[i:i+r],2)%2 != 0)


#assert odd_Equivalent("011001",6) == 3
#print(odd_Equivalent("011001",6))