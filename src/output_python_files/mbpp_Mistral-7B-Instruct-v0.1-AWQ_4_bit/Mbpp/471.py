"""
Write a python function to find the product of the array multiplication modulo n.
assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9
"""

def find_remainder(arr, n):
    """
    :param arr: array of integers
    :param n: modulo value
    :return: remainder of array multiplication modulo n
    """
    product = 1
    for i in range(len(arr)):
        product = (product * arr[i]) % n
    return product


if __name__ == '__main__':
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],11) ==9
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],12) ==11
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],13) ==12
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],14) ==13
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],15) ==14
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],16) ==15
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],17) ==16
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],18) ==17
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],19) ==18
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],20) ==19
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],21) ==20
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],22) ==21
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],23) ==22
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],24) ==23
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],25) ==24
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],26) ==25
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],27) ==26
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],28) ==27
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],29) ==28
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],30) ==29
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],31) ==30