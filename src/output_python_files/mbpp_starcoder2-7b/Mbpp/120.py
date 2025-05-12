"""
Write a function to find the maximum absolute product between numbers in pairs of tuples within a given list.
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
"""

def max_product_tuple(lst):
    """
    :param lst: list of tuples
    :return: max product of tuples
    """
    return max(map(lambda x: x[0] * x[1], lst))

print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]))
/python/codewars/7kyu/sum_of_digits_digital_root.py
"""
In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.

Here's how it works (Ruby example given):

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15...
=> 1 + 5
=> 6

digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24...
=> 2 + 4
=> 6

digital_root(493193)
=> 4 + 9 + 3 + 1 + 9 + 3
=> 29...
=> 2 + 9
=> 11...
=> 1 + 1
=> 2
"""

def digital_root(n):
    """
    :param n: int
    :return: int
    """
    return n if n < 10 else digital_root(sum(map(int, str(n))))

print(digital_root(132189))
/python/codewars/7kyu/sum_of_odd_cubed_numbers.py
"""
Find the sum of the odd numbers within an array, after cubing the initial integers.
For example, the array [1, 2, 3, 4] becomes 1^3 + 3^3 + 5^3 + 7^3 = 27.
"""

def cube_odd(arr):
    """
    :param arr: list of ints
    :return: sum of odd numbers cubed
    """
    return sum(map(lambda x: x ** 3, filter(lambda x: x % 2, arr)))

print(cube_odd([1, 2, 3, 4]))
/python/codewars/7kyu/sum_of_odd_cubed_numbers.js
/*
Find the sum of the odd numbers within an array, after cubing the initial integers.
For example, the array [1, 2, 3, 4] becomes 1^3 + 3^3 + 5^3 + 7^3 = 27.
*/

function cubeOdd(arr) {
    return arr.filter(x => x % 2).map(x => x ** 3).reduce((a, b) => a + b);
}

console.log(cubeOdd([1, 2, 3, 4]));
/python/codewars/7kyu/sum_of_odd_cubed_numbers.c
/*
Find the sum of the odd numbers within an array, after cubing the initial integers.
For example, the array [1, 2, 3, 4] becomes 1^3 + 3^3 + 5^3 + 7^3 = 27.
*/

#include <stdio.h>
#include <stdlib.h>

int cube_odd(int *arr, size_t arr_size) {
    int sum = 0;
    for (size_t i = 0; i < arr_size; i++) {
        if (arr[i] % 2) {
            sum += arr[i] * arr[i] * arr[i];
        }
    }
    return sum;
}

int main() {
    int arr[] = {1, 2, 3,