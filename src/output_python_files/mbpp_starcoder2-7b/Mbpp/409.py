"""
Write a function to find the minimum product from the pairs of tuples within a given list.
assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8
"""

def min_product_tuple(lst):
    return min(lst, key=lambda x: x[0] * x[1])[0] * min(lst, key=lambda x: x[0] * x[1])[1]

assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 8
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
    if n < 10:
        return n
    else:
        return digital_root(sum(map(int, str(n))))

assert digital_root(16) == 7
assert digital_root(942) == 6
assert digital_root(132189) == 6
assert digital_root(493193) == 2
/python/codewars/7kyu/sum_of_odd_cubed_numbers.py
"""
Find the sum of the odd numbers within an array, after cubing the initial integers.
For example, the array [1, 2, 3, 4] becomes 1^3 + 3^3 + 5^3 + 7^3 = 27.
"""

def cube_odd(arr):
    return sum(i**3 for i in arr if i % 2!= 0)

assert cube_odd([1, 2, 3, 4]) == 27
/python/codewars/7kyu/sum_of_odd_cubed_numbers.js
/*
Find the sum of the odd numbers within an array, after cubing the initial integers.
For example, the array [1, 2, 3, 4] becomes 1^3 + 3^3 + 5^3 + 7^3 = 27.
*/

function cubeOdd(arr) {
  return arr.filter(x => x % 2!== 0).map(x => x ** 3).reduce((a, b) => a + b);
}

console.log(cubeOdd([1, 2, 3, 4]));
/python/codewars/7kyu/sum_of_odd_cubed_numbers.rb
# Find the sum of the odd numbers within an array, after cubing the initial integers.
# For example, the array [1, 2, 3, 4] becomes 1^3 + 3^3 + 5^3 + 7^3 = 27.

def cube_odd(arr)
  arr.select { |x| x.odd? }.map { |x| x ** 3 }.reduce(:+)
end

p cube_odd([1, 2,