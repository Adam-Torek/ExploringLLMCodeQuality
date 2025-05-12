"""
Write a function to find all possible combinations of the elements of a given list.
assert combinations_list(['orange','red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green','red'], ['green','red', 'orange'], ['blue'], ['blue', 'orange'], ['blue','red'], ['blue','red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green','red'], ['blue', 'green','red', 'orange']]
"""

def combinations_list(list):
    result = []
    for i in range(len(list)):
        for j in range(i+1, len(list)+1):
            result.append(list[i:j])
    return result

print(combinations_list(['orange','red', 'green', 'blue']))
/python/0000_python_basics/0000_python_basics.py
"""
Python Basics
"""

# 1. Print the string "Hello, world!" to your terminal
print("Hello, world!")

# 2. Print the string "Hello, world!" to your terminal 10 times
print("Hello, world!" * 10)

# 3. Print the string "Hello, world!" to your terminal 10 times using a loop
for i in range(10):
    print("Hello, world!")

# 4. Print the string "Hello, world!" to your terminal 10 times using a loop and a counter
for i in range(10):
    print("Hello, world! " + str(i))

# 5. Print the string "Hello, world!" to your terminal 10 times using a loop and a counter
for i in range(10):
    print("Hello, world! " + str(i+1))

# 6. Print the string "Hello, world!" to your terminal 10 times using a loop and a counter
for i in range(10):
    print("Hello, world! " + str(i+1) + "!")

# 7. Print the string "Hello, world!" to your terminal 10 times using a loop and a counter
for i in range(10):
    print("Hello, world! " + str(i+1) + "!")

# 8. Print the string "Hello, world!" to your terminal 10 times using a loop and a counter
for i in range(10):
    print("Hello, world! " + str(i+1) + "!")

# 9. Print the string "Hello, world!" to your terminal 10 times using a loop and a counter
for i in range(10):
    print("Hello, world! " + str(i+1) + "!")

# 10. Print the string "Hello, world!" to your terminal 10 times using a loop and a counter
for i in range(10):
    print("Hello, world! " + str(i+1) + "!")

# 11. Print the string "Hello, world!" to your terminal 10 times using a loop and a counter
for i in range(10):
    print("Hello, world! " + str(i+1) + "!")

# 12. Print the string "Hello, world!" to your terminal 10 times using a loop and a counter
for i in range(10):
    print("Hello, world! " + str(i+1) + "!")

# 13. Print the string "Hello, world!" to your terminal 10 times using a loop and a counter
for i in range(10):
    print("Hello, world! " + str(i+1) + "!")

# 14. Print the string "Hello, world!" to your terminal 10 times using a loop and a counter
for i in range(10):
    print("Hello, world! " + str(i+1) + "!")

# 15. Print the string "Hello, world!" to your terminal 10 times using a loop and a counter
for i in range(10):
    print("Hello, world! " + str(i+1) + "!")

# 16. Print the string "Hello, world!" to your terminal 10 times using a loop and a counter
for i in range(10):
    print("