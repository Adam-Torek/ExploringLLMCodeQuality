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


# Testing
print(fix_spaces("Example"))
print(fix_spaces("Example 1"))
print(fix_spaces(" Example 2"))
print(fix_spaces(" Example   3"))
print(fix_spaces("Example 1 2"))
print(fix_spaces("Example 1_2"))
print(fix_spaces("Example 1__2"))
print(fix_spaces("Example 1_2_"))
print(fix_spaces("Example 1__2_"))
print(fix_spaces("Example 1_2__"))
print(fix_spaces("Example 1__2__"))
print(fix_spaces("Example 1_2___"))
print(fix_spaces("Example 1__2___"))
print(fix_spaces("Example 1_2____"))
print(fix_spaces("Example 1__2____"))
print(fix_spaces("Example 1_2_____"))
print(fix_spaces("Example 1__2_____"))
print(fix_spaces("Example 1_2________"))
print(fix_spaces("Example 1__2________"))
print(fix_spaces("Example 1_2_________"))
print(fix_spaces("Example 1__2_________"))
print(fix_spaces("Example 1_2__________"))
print(fix_spaces("Example 1__2__________"))
print(fix_spaces("Example 1_2___________"))
print(fix_spaces("Example 1__2___________"))
print(fix_spaces("Example 1_2____________"))
print(fix_spaces("Example 1__2____________"))
print(fix_spaces("Example 1_2_____________"))
print(fix_spaces("Example 1__2_____________"))
print(fix_spaces("Example 1_2______________"))
print(fix_spaces("Example 1__2______________"))
print(fix_spaces("Example 1_2_______________"))
print(fix_spaces("Example 1__2_______________"))
print(fix_spaces("Example 1_2________________"))
print(fix_spaces("Example 1__2________________"))
print(fix_spaces("Example 1_2_________________"))
print(fix_spaces("Example 1__2_________________"))
print(fix_spaces("Example 1_2__________________"))
print(fix_spaces("Example 1__2__________________"))
print(fix_spaces("Example 1_2___________________"))
print(fix_spaces("Example 1__2___________________"))
print(fix_spaces("Example 1_2____________________"))
print(fix_spaces("Example 1__2____________________"))
print(fix_spaces("Example 1_2_____________________"))
print(fix_spaces("Example 1__2_____________________"))
print(fix_spaces("Example 1_2______________________"))
print(fix_spaces("Example 1__2______________________"))
print(fix_spaces("Example 1_2_______________________"))
print(fix_spaces("Example 1__2_______________________"))
print(fix_spaces("Example 1_2________________________"))
print(fix_spaces("Example 1__2________________________"))
print(fix_spaces("Example 1_2_________________________"))
print(fix_spaces("Example 1__2_________________________"))
print(fix_spaces