"""
Write a function that takes in a string and character, replaces blank spaces in the string with the character, and returns the string.
assert replace_blank("hello people",'@')==("hello@people")
"""

def replace_blank(string, char):
    return string.replace(" ", char)

print(replace_blank("hello people", "@"))
<file_sep>/python/python_fundamentals/for_loop_basic2.py
"""
Basic - Print all integers from 0 to 150.

Multiples of Five - Print all the multiples of 5 from 5 to 1,000

Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR loop. For (2,9,3), print 3 6 9 (on successive lines)

The Final Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print the final number counted, and how many times this was counted. For (2,9,3), print "Final countdown is 9. 8 counts."
"""

# Basic - Print all integers from 0 to 150.
for i in range(151):
    print(i)

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for i in range(5, 1001, 5):
    print(i)

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(1, 101):
    if i % 5 == 0 and i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
sum = 0
for i in range(0, 500001, 2):
    sum += i
print(sum)

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for i in range(2018, 0, -4):
    print(i)

# Flexible Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print multiples of mult from lowNum to highNum, using a FOR loop. For (2,9,3), print 3 6 9 (on successive lines)
for i in range(2, 10, 3):
    print(i)

# The Final Countdown - Based on earlier "Countdown by Fours", given lowNum, highNum, mult, print the final number counted, and how many times this was counted. For (2,9,3), print "Final countdown is 9. 8 counts."
count = 0
for i in range(2, 10, 3):
    count += 1
print("Final countdown is 9. {} counts.".format(count))
<file_sep>/python/python_fundamentals/coin_tosses.py
"""
Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
"""

import random

def coin_tosses():
    heads = 0
    tails = 0
    for i in range(1, 5001):
        toss = random.randint(0, 1)
        if toss == 0:
            heads += 1
        else:
            tails += 1
    print("Heads: {}, Tails: {}".format(heads, tails))

coin_tosses()
<file_sep>/python