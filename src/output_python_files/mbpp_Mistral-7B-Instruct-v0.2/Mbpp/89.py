"""
Write a function to find the closest smaller number than n.
assert closest_num(11) == 10
"""

def closest_num(n):
    """
    :type n: int
    :rtype: int
    """
    smaller_num = n
    for i in range(n, 0, -1):
        if i < n and i > smaller_num:
            smaller_num = i
    return smaller_num

if __name__ == "__main__":
    assert closest_num(11) == 10
    assert closest_num(10) == 9
    assert closest_num(5) == 5
    assert closest_num(1) == 1
    assert closest_num(0) == 0
    assert closest_num(100) == 99
    assert closest_num(1000) == 999
    assert closest_num(float('inf')) == float('inf')
    assert closest_num(float('-inf')) == float('-inf')