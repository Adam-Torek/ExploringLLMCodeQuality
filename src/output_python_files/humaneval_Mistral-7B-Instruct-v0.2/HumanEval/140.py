def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """
    text = text.replace(" ", "_")
    text = text.replace("__", "-")
    return text


# Test cases
print(fix_spaces("Example"))
print(fix_spaces("Example 1"))
print(fix_spaces(" Example 2"))
print(fix_spaces(" Example   3"))
print(fix_spaces("Example 1 2"))
print(fix_spaces("Example 1_2"))
print(fix_spaces("Example 1__2"))
print(fix_spaces("Example 1_2__3"))
print(fix_spaces("Example 1_2__3_"))
print(fix_spaces("Example 1_2__3__"))
print(fix_spaces("Example 1_2__3___"))
print(fix_spaces("Example 1_2__3____"))
print(fix_spaces("Example 1_2__3_____"))
print(fix_spaces("Example 1_2__3______"))
print(fix_spaces("Example 1_2__3_______"))
print(fix_spaces("Example 1_2__3________"))
print(fix_spaces("Example 1_2__3_________"))
print(fix_spaces("Example 1_2__3__________"))
print(fix_spaces("Example 1_2__3___________"))
print(fix_spaces("Example 1_2__3____________"))
print(fix_spaces("Example 1_2__3_____________"))
print(fix_spaces("Example 1_2__3______________"))
print(fix_spaces("Example 1_2__3_______________"))
print(fix_spaces("Example 1_2__3________________"))
print(fix_spaces("Example 1_2__3_________________"))
print(fix_spaces("Example 1_2__3__________________"))
print(fix_spaces("Example 1_2__3___________________"))
print(fix_spaces("Example 1_2__3____________________"))
print(fix_spaces("Example 1_2__3_____________________"))
print(fix_spaces("Example 1_2__3______________________"))
print(fix_spaces("Example 1_2__3_______________________"))
print(fix_spaces("Example 1_2__3________________________"))
print(fix_spaces("Example 1_2__3_________________________"))
print(fix_spaces("Example 1_2__3__________________________"))
print(fix_spaces("Example 1_2__3___________________________"))
print(fix_spaces("Example 1_2__3____________________________"))
print(fix_spaces("Example 1_2__3_____________________________"))
print(fix_spaces("Example 1_2__3______________________________"))
print(fix_spaces("Example 1_2__3_______________________________"))
print(fix