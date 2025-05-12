"""
Write a python function to check whether all the characters are same or not.
assert all_Characters_Same("python") == False
"""

def all_Characters_Same(string):
    for i in range(len(string)-1):
        if string[i]!= string[i+1]:
            return False
    return True

print(all_Characters_Same("python"))
print(all_Characters_Same("pppp"))
print(all_Characters_Same("ppppp"))
print(all_Characters_Same("pppppp"))
print(all_Characters_Same("ppppppp"))
print(all_Characters_Same("pppppppp"))
print(all_Characters_Same("ppppppppp"))
print(all_Characters_Same("pppppppppp"))
print(all_Characters_Same("ppppppppppp"))
print(all_Characters_Same("pppppppppppp"))
print(all_Characters_Same("ppppppppppppp"))
print(all_Characters_Same("pppppppppppppp"))
print(all_Characters_Same("ppppppppppppppp"))
print(all_Characters_Same("pppppppppppppppp"))
print(all_Characters_Same("ppppppppppppppppp"))
print(all_Characters_Same("pppppppppppppppppp"))
print(all_Characters_Same("ppppppppppppppppppp"))
print(all_Characters_Same("pppppppppppppppppppp"))
print(all_Characters_Same("ppppppppppppppppppppp"))
print(all_Characters_Same("pppppppppppppppppppppp"))
print(all_Characters_Same("ppppppppppppppppppppppp"))
print(all_Characters_Same("pppppppppppppppppppppppp"))
print(all_Characters_Same("ppppppppppppppppppppppppp"))
print(all_Characters_Same("pppppppppppppppppppppppppp"))
print(all_Characters_Same("ppppppppppppppppppppppppppp"))
print(all_Characters_Same("pppppppppppppppppppppppppppp"))
print(all_Characters_Same("ppppppppppppppppppppppppppppp"))
print(all_Characters_Same("pppppppppppppppppppppppppppppp"))
print(all_Characters_Same("ppppppppppppppppppppppppppppppp"))
print(all_Characters_Same("pppppppppppppppppppppppppppppppp"))
print(all_Characters_Same("ppppppppppppppppppppppppppppppppp"))
print(all_Characters_Same("pppppppppppppppppppppppppppppppppp"))
print(all_Characters_Same("ppppppppppppppppppppppppppppppppppp"))
print(all_Characters_Same("pppppppppppppppppppppppppppppppppppp"))
print(all_Characters_Same("ppppppppppppppppppppppppppppppppppppp"))
print(all_Characters_Same("pppppppppppppppppppppppppppppppppppppp"))
print(all_Characters_Same("ppppppppppppppppppppppppppppppppppppppp"))
print(all_Characters_Same("pppppppppppppppppppppppppppppppppppppppp"))
print(all_Characters_Same("ppppppppppppppppppppppppppppppppppppppppp"))
print(all_Characters_Same("pppppppppppppppppppppppppppppppppppppppppp"))
print(all_Characters_Same("ppppppppppppppppppppppppppppppppppppppppppp"))
print(all_Characters_Same("pppppppppppppppppppppppppppppppppppppppppppp"))
print(all_Characters_Same("pppppppppppppppppppppppppppppppppppp