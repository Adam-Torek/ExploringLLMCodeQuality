"""
Write a function to count number items that are identical in the same position of three given lists.
assert count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9])==3
"""
def count_samepair(list1,list2,list3):
    count=0
    for i in range(len(list1)):
        if list1[i]==list2[i]==list3[i]:
            count+=1
    return count

print(count_samepair([1,2,3,4,5,6,7,8],[2,2,3,1,2,6,7,9],[2,1,3,1,2,6,7,9]))
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_1.py
"""
Write a program that asks the user to enter a number and prints the square of that number.
"""

number=int(input("Enter a number: "))
print("The square of the number is: ",number**2)
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_2.py
"""
Write a program that asks the user to enter a number and prints the square root of that number.
"""

number=int(input("Enter a number: "))
print("The square root of the number is: ",number**0.5)
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_3.py
"""
Write a program that asks the user to enter a number and prints the cube of that number.
"""

number=int(input("Enter a number: "))
print("The cube of the number is: ",number**3)
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_4.py
"""
Write a program that asks the user to enter a number and prints the fourth power of that number.
"""

number=int(input("Enter a number: "))
print("The fourth power of the number is: ",number**4)
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_5.py
"""
Write a program that asks the user to enter a number and prints the fifth power of that number.
"""

number=int(input("Enter a number: "))
print("The fifth power of the number is: ",number**5)
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_6.py
"""
Write a program that asks the user to enter a number and prints the sixth power of that number.
"""

number=int(input("Enter a number: "))
print("The sixth power of the number is: ",number**6)
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_7.py
"""
Write a program that asks the user to enter a number and prints the seventh power of that number.
"""

number=int(input("Enter a number: "))
print("The seventh power of the number is: ",number**7)
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_8.py
"""
Write a program that asks the user to enter a number and prints the eighth power of that number.
"""

number=int(input("Enter a number: "))
print("The eighth power of the number is: ",number**8)
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_9.py
"""
Write a program that asks the user to enter a number and prints the ninth power of that number.
"""

number=int(input("Enter a number: "))
print("The ninth power of the number is: ",number**9)
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_10.py
"""
Write a program that asks the user to enter a number and prints the tenth power of that number.
"""

number=int(input("Enter a number: "))
print("The tenth power of the number is: ",number**10)
<file_sep>/Python/Python_Basics/Python_Basics_1/Python_Basics_1_11.py
"""
Write a program that asks the user to