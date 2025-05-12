"""
Write a function to multiply all the numbers in a list and divide with the length of the list.
assert math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001)
"""
def multiply_num(list):
    return reduce(lambda x, y: x*y, list)/len(list)

"""
Write a function to find the factorial of a number.
assert factorial(5) == 120
"""
def factorial(num):
    return reduce(lambda x, y: x*y, range(1, num+1))

"""
Write a function to find the mean of a list of numbers.
assert math.isclose(mean([1, 0, 3, 3, 5, 6, 6, 7, 7]), 4.333333333333333, rel_tol=0.001)
"""
def mean(list):
    return reduce(lambda x, y: x+y, list)/len(list)

"""
Write a function to find the median of a list of numbers.
assert math.isclose(median([1, 3, 3, 6, 7, 8, 9]), 6, rel_tol=0.001)
"""
def median(list):
    list.sort()
    if len(list)%2 == 0:
        return (list[len(list)/2] + list[len(list)/2 - 1])/2
    else:
        return list[len(list)/2]

"""
Write a function to find the mode of a list of numbers.
assert mode([1, 2, 3, 3, 3, 3, 4, 5]) == 3
"""
def mode(list):
    return max(set(list), key=list.count)

"""
Write a function to find the geometric mean of a list of numbers.
assert math.isclose(geometric_mean([4, 3, 2, 6]), 3.779644730092272, rel_tol=0.001)
"""
def geometric_mean(list):
    return reduce(lambda x, y: x*y, list)**(1/len(list))

"""
Write a function to find the harmonic mean of a list of numbers.
assert math.isclose(harmonic_mean([2, 6, 9, 18]), 5.277777777777778, rel_tol=0.001)
"""
def harmonic_mean(list):
    return len(list)/reduce(lambda x, y: x+1/y, list)

"""
Write a function to find the standard deviation of a list of numbers.
assert math.isclose(standard_deviation([4, 3, 2, 6]), 1.4696939061993909, rel_tol=0.001)
"""
def standard_deviation(list):
    return (reduce(lambda x, y: x+y, map(lambda x: (x - mean(list))**2, list))/(len(list)-1))**0.5

"""
Write a function to find the variance of a list of numbers.
assert math.isclose(variance([4, 3, 2, 6]), 2.083333333333333, rel_tol=0.001)
"""
def variance(list):
    return reduce(lambda x, y: x+y, map(lambda x: (x - mean(list))**2, list))/(len(list)-1)

"""
Write a function to find the covariance of two lists of numbers.
assert math.isclose(covariance([4, 3, 2, 6], [1, 2, 3, 4]), 0.6666666666666666, rel_tol=0.001)
"""
def covariance(list1, list2):
    return reduce(lambda x, y: x+y, map(lambda x, y: (x - mean(list1))*(y - mean(list2)), list1, list2))