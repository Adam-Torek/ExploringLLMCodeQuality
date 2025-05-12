"""
Write a function to find the product of first even and odd number of a given list.
assert mul_even_odd([1,3,5,7,4,1,6,8])==4
"""
def mul_even_odd(numbers):
    """
    Function to find the product of first even and odd number of a given list
    :param numbers: list of numbers
    :return: product of first even and odd number
    """
    even_numbers = []
    odd_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    if len(even_numbers) > 0 and len(odd_numbers) > 0:
        return even_numbers[0] * odd_numbers[0]
    else:
        raise ValueError("List should have at least one even and one odd number")

if __name__ == "__main__":
    assert mul_even_odd([1,3,5,7,4,1,6,8]) == 4
    assert mul_even_odd([2,3,5,7,4,1,6,8]) == 12
    assert mul_even_odd([1,2,5,7,4,1,6,8]) == 2
    assert mul_even_odd([1,3,5,7,4,1,6]) == ValueError
    assert mul_even_odd([1,3,5,7,4,1]) == ValueError
    assert mul_even_odd([1,3,5,7,4]) == ValueError
    assert mul_even_odd([1,3,5]) == ValueError
    assert mul_even_odd([1,3]) == ValueError
    assert mul_even_odd([1]) == ValueError
    assert mul_even_odd([]) == ValueError
    assert mul_even_odd([2]) == 2
    assert mul_even_odd([2,2]) == 2
    assert mul_even_odd([2,2,2]) == 2
    assert mul_even_odd([2,2,2,2]) == 2
    assert mul_even_odd([2,2,2,2,2]) == 2
    assert mul_even_odd([2,2,2,2,2,2]) == 2
    assert mul_even_odd([2,2,2,2,2,2,2]) == 2
    assert mul_even_odd([2,2,2,2,2,2,2,2]) == 2
    assert mul_even_odd([2,2,2,2,2,2,2,2,2]) == 2
    assert mul_even_odd([2,2,2,2,2,2,2,2,2,2]) == 2
    assert mul_even_odd([2,2,2,2,2,2,2,2,2,2,2]) == 2
    assert mul_even_odd([2,2,2,2,2,2,2,2,2,2,2,2]) == 2
    assert mul_even_odd([2,2,2,2,2,2,2,2,2,2,2,2,2]) == 2
    assert mul_even_odd([2,2,2,2,2,2,2,2,2,2,2,2,2,2]) == 2
    assert mul_even_odd([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]) == 2
    assert mul_even_odd([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]) == 2
    assert mul_even_odd([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]) == 2
    assert mul_even_odd([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]) == 2
    assert mul_even_odd([2,2,2,2