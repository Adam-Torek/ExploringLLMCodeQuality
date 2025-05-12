"""
Write a python function to split a list at the nth eelment and add the first part to the end.
assert split_Arr([12,10,5,6,52,36],2) == [5,6,52,36,12,10]
"""

def split_Arr(arr,n):
    return arr[n:] + arr[:n]

print(split_Arr([12,10,5,6,52,36],2))/Python/Python_Fundamentals/Functions_Intermediate_I/Functions_Intermediate_I.py
"""
Functions Intermediate I
"""

# 1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
   'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

# 2. Iterate Through a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(arr):
    for i in range(len(arr)):
        print(f"{i+1} - {arr[i]['first_name']} {arr[i]['last_name']}")

iterateDictionary(students)

# 3. Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# 4. Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict:
        print(f"{key.upper()}:")
        for i in range(len(some_dict[key])):
            print(f"{i+1} - {some_dict[key][i]}")

printInfo(dojo)/Python/Python_Fundamentals/Functions_Basic_II/Functions_Basic_II.py
"""
Functions Basic II
"""

# 1. Countdown
def countdown(num):
    for i in range(num, -1, -1):
        print(i)

countdown(5)

# 2. Print and Return
def print_and_return(arr):
    print(arr[0])
    return arr[1]

print_and_return([1,2])

# 3. First Plus Length
def first_plus_length(arr):
    return arr[0] + len(arr)