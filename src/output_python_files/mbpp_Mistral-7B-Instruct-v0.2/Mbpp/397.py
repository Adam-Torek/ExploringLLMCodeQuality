"""
Write a function to find the median of three numbers.
assert median_numbers(25,55,65)==55.0
"""
def median_numbers(num1, num2, num3):
    """
    Find the median of three numbers
    :param num1: first number
    :param num2: second number
    :param num3: third number
    :return: median value
    """
    numbers = [num1, num2, num3]
    numbers.sort()
    if len(numbers) % 2 == 0:
        median = (numbers[len(numbers)//2] + numbers[len(numbers)//2-1])/2
    else:
        median = numbers[len(numbers)//2]
    return median

assert median_numbers(25,55,65)==55.0
assert median_numbers(1,2,3)==2.0
assert median_numbers(1,2,3,4)==2.5
assert median_numbers(1,2,3,4,5)==3.0</s>