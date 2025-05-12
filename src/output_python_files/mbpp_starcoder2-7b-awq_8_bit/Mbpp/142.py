"""
Write a function to count number items that are identical in the same position of three given lists.
assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
"""

def count_samepair(list1, list2, list3):
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i] == list3[i]:
            count += 1
    return count

print(count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9]))/python_fundamentals/for_loop_basic2.py
"""
Write a function that counts from 1 to 2000. 
As it loops through each number, have your program print "Even" if the number is even, 
or "Odd" if the number is odd.
"""

def count_to_2000():
    for i in range(1, 2001):
        if i % 2 == 0:
            print("Even")
        else:
            print("Odd")

count_to_2000()/python_fundamentals/for_loop_basic1.py
"""
Write a function that prints all the integers from 0 to 150. 
Have the function count by 5's. (Even though 150 is not included, 
it should still print it since it is always included).
"""

def count_to_150():
    for i in range(0, 151, 5):
        print(i)

count_to_150()/python_fundamentals/for_loop_basic3.py
"""
Write a function that prints the integers from 0 to 1000. 
Have the function count by fours, 
but for multiples of five print "Coding" instead of the number. 
For multiples of both three and five print, "Coding Dojo".
"""

def count_to_1000():
    for i in range(0, 1001, 4):
        if i % 5 == 0:
            print("Coding")
        elif i % 3 == 0:
            print("Coding Dojo")
        else:
            print(i)

count_to_1000()/python_fundamentals/for_loop_basic4.py
"""
Write a function that prints the multiples of 3 from 0 to 1000. 
Have a separate except at 300. 
(Use a loop of your choice, not a range function.)
"""

def count_to_1000():
    for i in range(0, 1001, 3):
        if i == 300:
            print("Done")
        else:
            print(i)

count_to_1000()/python_fundamentals/for_loop_basic5.py
"""
Write a function that prints the multiples of 5 from 5 to 1,000,000. 
Have a separate except at 25,000,000. 
(Use a loop of your choice, not a range function.)
"""

def count_to_1000000():
    for i in range(5, 1000000, 5):
        if i == 25000000:
            print("Done")
        else:
            print(i)

count_to_1000000()/python_fundamentals/for_loop_basic6.py
"""
Write a function that prints the odd numbers from 1 to 1000. 
Use a FOR LOOP and not a WHILE LOOP.
"""

def count_to_1000():
    for i in range(1, 1001, 2):
        print(i)

count_to_1000()/python_fundamentals/for_loop_basic7.py
"""
Write a function that prints the multiples of 6 from 0 to 1000000