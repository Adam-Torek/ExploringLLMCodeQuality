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
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],12) ==10
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],13) ==11
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],14) ==12
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],15) ==13
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],16) ==14
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],17) ==15
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],18) ==16
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],19) ==17
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],20) ==18
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],21) ==19
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],22) ==20
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],23) ==21
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],24) ==22
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],25) ==23
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],26) ==24
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],27) ==25
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],28) ==26
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],29) ==27
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],30) ==28
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],31) ==29
    assert find_remainder([ 100, 10, 5, 25, 35, 14 ],32) ==30
    assert find_remainder([