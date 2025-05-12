"""
Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
assert index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]) == 'Varsha'
"""

def index_minimum(lst):
    min_val = lst[0][1]
    min_index = 0
    for i in range(1, len(lst)):
        if lst[i][1] < min_val:
            min_val = lst[i][1]
            min_index = i
    return lst[min_index][0]

print(index_minimum([('Rash', 143), ('Manjeet', 200), ('Varsha', 100)]))/python_fundamentals/for_loop_basic2.py
"""
Print integers from 0 to 100. 
But for multiples of five print "Coding" instead of the number and for multiples of fifteen print "Coding Dojo".
"""

for i in range(0, 101):
    if i % 5 == 0 and i % 15 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)/python_fundamentals/coin_toss.py
"""
Create a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.
Sample output should be like this:
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
Attempt #10: Throwing a coin... It's a tail!... Got 6 head(s) so far and 4 tail(s) so far
Attempt #11: Throwing a coin... It's a head!... Got 7 head(s) so far and 4 tail(s) so far
Attempt #12: Throwing a coin... It's a tail!... Got 7 head(s) so far and 5 tail(s) so far
Attempt #13: Throwing a coin... It's a head!... Got 8 head(s) so far and 5 tail(s) so far
Attempt #14: Throwing a coin... It's a tail!... Got 8 head(s) so far and 6 tail(s) so far
Attempt #15: Throwing a coin... It's a head!... Got 9 head(s) so far and 6 tail(s) so far
Attempt #16: Throwing a coin... It's a tail!... Got 9 head(s) so far and 7 tail(s) so far
Attempt #17: Throwing a coin... It's a head!... Got 10 head(s) so far and 7 tail(s) so far
Attempt #18: Throwing a coin... It's a tail!... Got 10 head(s) so far and 8 tail(s) so far
Attempt #19: Throwing a coin... It's a head!... Got 11 head(s) so far and 8 tail(s) so