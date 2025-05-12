"""
Write a python function to count the number of substrings with the sum of digits equal to their length.
assert count_Substrings('112112') == 6
"""

def count_Substrings(string):
    count = 0
    for i in range(len(string)):
        for j in range(i, len(string)):
            if sum(map(int, string[i:j+1])) == len(string[i:j+1]):
                count += 1
    return count

print(count_Substrings('112112'))
/Python/CodeWars/7kyu/sum_of_digits_digital_root.py
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

print(digital_root(132189))
/Python/CodeWars/7kyu/sum_of_odd_numbers.py
"""
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8
"""

def row_sum_odd_numbers(n):
    return sum(range(1, n*2+1, 2))

print(row_sum_odd_numbers(1))
/Python/CodeWars/7kyu/sum_of_digits_digital_root.js
/*
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
*/

function digital_root(n) {
  if (n < 10) {
    return n;
  } else {
    return digital_root(n.toString().split('').reduce((a, b) => parseInt(a) + parseInt(b)));
  }
}

console.log(digital_root(132189));
/Python/CodeWars/7kyu/sum_of