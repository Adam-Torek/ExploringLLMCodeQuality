"""
Write a function to find the maximum absolute product between numbers in pairs of tuples within a given list.
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
"""

def max_product_tuple(tuples):
    """
    tuples: a list of tuples
    """
    # Your code here
    max_product = 0
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            max_product = max(max_product, abs(tuples[i][0]*tuples[j][1] - tuples[i][1]*tuples[j][0]))
    return max_product


def max_product_tuple_2(tuples):
    """
    tuples: a list of tuples
    """
    # Your code here
    max_product = 0
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            max_product = max(max_product, abs(tuples[i][0]*tuples[j][1] - tuples[i][1]*tuples[j][0]))
    return max_product


def max_product_tuple_3(tuples):
    """
    tuples: a list of tuples
    """
    # Your code here
    max_product = 0
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            max_product = max(max_product, abs(tuples[i][0]*tuples[j][1] - tuples[i][1]*tuples[j][0]))
    return max_product


def max_product_tuple_4(tuples):
    """
    tuples: a list of tuples
    """
    # Your code here
    max_product = 0
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            max_product = max(max_product, abs(tuples[i][0]*tuples[j][1] - tuples[i][1]*tuples[j][0]))
    return max_product


def max_product_tuple_5(tuples):
    """
    tuples: a list of tuples
    """
    # Your code here
    max_product = 0
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            max_product = max(max_product, abs(tuples[i][0]*tuples[j][1] - tuples[i][1]*tuples[j][0]))
    return max_product


def max_product_tuple_6(tuples):
    """
    tuples: a list of tuples
    """
    # Your code here
    max_product = 0
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            max_product = max(max_product, abs(tuples[i][0]*tuples[j][1] - tuples[i][1]*tuples[j][0]))
    return max_product


def max_product_tuple_7(tuples):
    """
    tuples: a list of tuples
    """
    # Your code here
    max_product = 0
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            max_product = max(max_product, abs(tuples[i][0]*tuples[j][1] - tuples[i][1]*tuples[j][0]))
    return max_product


def max_product_tuple_8(tuples):
    """
    tuples: a list of tuples
    """
    # Your code here
    max_product = 0
    for i in range(len(tuples)):
        for j in range(i+1, len(tuples)):
            max_product = max(max_product, abs(tuples[i][0]*tuples[j][1] - tuples[i][1]*tu