"""
Write a function to convert more than one list to nested dictionary.
assert convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"],[85, 98, 89, 92])==[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
"""

def convert_list_dictionary(list1,list2,list3):
    dict1={}
    dict2={}
    dict3={}
    for i in range(len(list1)):
        dict1[list1[i]]=list2[i]
        dict2[list1[i]]=list3[i]
    dict3[list1[0]]=dict1
    dict3[list1[1]]=dict2
    dict3[list1[2]]=dict3
    return dict3

print(convert_list_dictionary(["S001", "S002", "S003", "S004"],["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"],[85, 98, 89, 92]))
/Python_Practice/Python_Practice_1/Python_Practice_1_1.py
"""
Write a function to convert a list of strings to a list of integers.
assert convert_list_to_int(["1", "2", "3", "4"])==[1, 2, 3, 4]
"""

def convert_list_to_int(list1):
    list2=[]
    for i in list1:
        list2.append(int(i))
    return list2

print(convert_list_to_int(["1", "2", "3", "4"]))
/Python_Practice/Python_Practice_1/Python_Practice_1_2.py
"""
Write a function to convert a list of integers to a list of strings.
assert convert_list_to_string([1, 2, 3, 4])==["1", "2", "3", "4"]
"""

def convert_list_to_string(list1):
    list2=[]
    for i in list1:
        list2.append(str(i))
    return list2

print(convert_list_to_string([1, 2, 3, 4]))
/Python_Practice/Python_Practice_1/Python_Practice_1_3.py
"""
Write a function to convert a list of strings to a list of floats.
assert convert_list_to_float(["1", "2", "3", "4"])==[1.0, 2.0, 3.0, 4.0]
"""

def convert_list_to_float(list1):
    list2=[]
    for i in list1:
        list2.append(float(i))
    return list2

print(convert_list_to_float(["1", "2", "3", "4"]))
/Python_Practice/Python_Practice_1/Python_Practice_1_4.py
"""
Write a function to convert a list of strings to a list of booleans.
assert convert_list_to_boolean(["1", "2", "3", "4"])==[True, True, True, True]
"""

def convert_list_to_boolean(list1):
    list2=[]
    for i in list1:
        list2.append(bool(i))
    return list2

print(convert_list_to_boolean(["1", "2", "3", "4"]))
/Python_Practice/Python_Practice_1/Python_Practice_1_5.py
"""
Write a function to convert a list of strings to a list of lists.
assert convert_list_to_list(["1", "2", "3", "4"])==[[1], [2], [3], [4]]
"""

def convert_list_to_list(list1):
    list2=[]
    for i in list1:
        list2.append([