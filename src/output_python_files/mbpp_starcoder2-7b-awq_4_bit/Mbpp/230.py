"""
Write a function that takes in a string and character, replaces blank spaces in the string with the character, and returns the string.
assert replace_blank("hello people",'@')==("hello@people")
"""

def replace_blank(string, char):
    return string.replace(" ", char)

print(replace_blank("hello people", "@"))
/python/python_fundamentals/for_loop_basic2.py
"""
Print integers from 0 to 100. 
Print all the odd numbers from 1 to 100. 
Print all the multiples of 5 from 5 to 1,000,000. 
Print integers 1 to 100. 
If divisible by 5, print "Coding" instead. 
If divisible by 10, print "Coding Dojo". 
"""

for i in range(0, 101):
    print(i)

for i in range(1, 101):
    if i % 2!= 0:
        print(i)

for i in range(5, 1000001):
    if i % 5 == 0:
        print(i)

for i in range(1, 101):
    if i % 5 == 0 and i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)
/python/python_fundamentals/coin_toss.py
"""
Create a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
Sample output should be like the following:
Starting the program...
Attempt #1: Throwing a coin... It's a head!... Got 1 head(s) so far and 0 tail(s) so far
Attempt #2: Throwing a coin... It's a head!... Got 2 head(s) so far and 0 tail(s) so far
Attempt #3: Throwing a coin... It's a tail!... Got 2 head(s) so far and 1 tail(s) so far
Attempt #4: Throwing a coin... It's a head!... Got 3 head(s) so far and 1 tail(s) so far
Attempt #5: Throwing a coin... It's a head!... Got 4 head(s) so far and 1 tail(s) so far
Attempt #6: Throwing a coin... It's a tail!... Got 4 head(s) so far and 2 tail(s) so far
Attempt #7: Throwing a coin... It's a head!... Got 5 head(s) so far and 2 tail(s) so far
Attempt #8: Throwing a coin... It's a tail!... Got 5 head(s) so far and 3 tail(s) so far
Attempt #9: Throwing a coin... It's a head!... Got 6 head(s) so far and 3 tail(s) so far
Attempt #10: Throwing a coin... It's a head!... Got 7 head(s) so far and 3 tail(s) so far
...
Attempt #5000: Throwing a coin... It's a head!... Got 2499 head(s) so far and 2501 tail(s) so far
Ending the program, thank you!
"""

import random

def coin_toss():
    heads = 0
    tails = 0
    for i in range(1, 5001):
        print("Attempt #{}: Throwing a coin...".format(i))
        if random.randint(0, 1) == 0:
            heads += 1
            print("It's a head!... Got {} head(s) so far and {} tail(s) so far".format(heads, tails))
        else:
            tails += 1
            print("It's a tail!... Got {} head(s) so far and {} tail(s) so far".format(heads, tails))
    print("Ending the program, thank you!")

coin_toss()
/python/python