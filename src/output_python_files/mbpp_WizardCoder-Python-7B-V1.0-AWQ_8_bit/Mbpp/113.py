"""
Write a function to check if a string represents an integer or not.
assert check_integer("python")==False
"""
def check_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

# Test cases
print(check_integer("python")) # False
print(check_integer("123")) # True
print(check_integer("-123")) # True
print(check_integer("+123")) # True
print(check_integer("0")) # True
print(check_integer("0000001")) # True
print(check_integer("123.456")) # False
print(check_integer("123a")) # False
print(check_integer("123!")) # False
print(check_integer("123 456")) # False
print(check_integer("123\n456")) # False
print(check_integer("123\t456")) # False
print(check_integer("123\r456")) # False
print(check_integer("123\x0b456")) # False
print(check_integer("123\x1c456")) # False
print(check_integer("123\x7f456")) # False
print(check_integer("123\x08456")) # False
print(check_integer("123\x0b456")) # False
print(check_integer("123\x1c456")) # False
print(check_integer("123\x7f456")) # False
print(check_integer("123\x8f456")) # False
print(check_integer("123\x9f456")) # False
print(check_integer("123\ufeff456")) # False
print(check_integer("123\uffff456")) # False
print(check_integer("123\uff10456")) # False
print(check_integer("123\u0800456")) # False
print(check_integer("123\u007f456")) # False
print(check_integer("123\u0080456")) # False
print(check_integer("123\u008f456")) # False
print(check_integer("123\u009f456")) # False
print(check_integer("123\uffff456")) # False
print(check_integer("123\U000100000456")) # False
print(check_integer("123\U00010000f456")) # False
print(check_integer("123\U0001000000456")) # False
print(check_integer("123\U00010000f456")) # False
print(check_integer("123\U00010fffe456")) # False
print(check_integer("123\U00010ffff456")) # False
print(check_integer("123\U0001100000456")) # False
print(check_integer("123\U00011000f456")) # False
print(check_integer("123\U0001100000456")) # False
print(check_integer("123\U00011000f456")) # False
print(check_integer("123\U0001100000456")) # False
print(check_integer("123\U00011000f456")) # False
print(check_integer("123\U0001100000456")) # False
print(check_integer("123\U00011000f456")) # False
print(check_integer("123\U0001