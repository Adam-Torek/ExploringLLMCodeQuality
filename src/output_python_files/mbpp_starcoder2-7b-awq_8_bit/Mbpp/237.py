"""
Write a function that takes in a list of tuples and returns a dictionary mapping each unique tuple to the number of times it occurs in the list.
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
"""

def check_occurences(lst):
    d = {}
    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

print(check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]))
/python/codewars/7kyu/find_the_odd_int.py
"""
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

assert find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5
"""

def find_it(seq):
    for i in seq:
        if seq.count(i) % 2!= 0:
            return i

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
/python/codewars/7kyu/find_the_odd_int.js
/*
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

assert findIt([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5
*/

function findIt(seq) {
  for (let i = 0; i < seq.length; i++) {
    if (seq.indexOf(seq[i]) === seq.lastIndexOf(seq[i])) {
      return seq[i];
    }
  }
}

console.log(findIt([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]));
/python/codewars/7kyu/find_the_odd_int.c
/*
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

assert findIt([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5
*/

#include <stdio.h>

int findIt(int seq[], int n) {
  int i, j, count;
  for (i = 0; i < n; i++) {
    count = 0;
    for (j = 0; j < n; j++) {
      if (seq[i] == seq[j]) {
        count++;
      }
    }
    if (count % 2!= 0) {
      return seq[i];
    }
  }
}

int main() {
  int seq[] = {20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5};
  int n = sizeof(seq) / sizeof(seq[0]);
  printf("%d\n", findIt(seq, n));
  return 0;
}
/python/codewars/7kyu/find_the_odd_int.rb
=begin
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

assert find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]) == 5
=end

def find_it(seq)
  seq.each do |i|
    if seq.count(i) % 2!= 0
      return i
    end
  end
end