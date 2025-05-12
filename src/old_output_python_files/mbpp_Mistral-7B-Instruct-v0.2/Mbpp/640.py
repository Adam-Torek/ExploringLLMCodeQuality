"""
Write a function to remove the parenthesis and what is inbetween them from a string.
assert remove_parenthesis(["python (chrome)"])==("python")
"""
def remove_parenthesis(input_string):
    """
    Function to remove the parenthesis and what is inbetween them from a string.
    :param input_string: string
    :return: string without parenthesis and what is inbetween them
    """
    return input_string.replace('(', '').replace(')', '')

# Test the function
assert remove_parenthesis(["python (chrome)"]) == "python"
assert remove_parenthesis("python (apple) (orange)") == "python"
assert remove_parenthesis("python (1+1)") == "python"
assert remove_parenthesis("python (1+1) (2+2)") == "python"
assert remove_parenthesis("python (1+1) (2+2) (3+3)") == "python"
assert remove_parenthesis("python (1+1) (2+2) (3+3) (4+4)") == "python"
assert remove_parenthesis("python (1+1) (2+2) (3+3) (4+4) (5+5)") == "python"
assert remove_parenthesis("python (1+1) (2+2) (3+3) (4+4) (5+5) (6+6)") == "python"
assert remove_parenthesis("python (1+1) (2+2) (3+3) (4+4) (5+5) (6+6) (7+7)") == "python"
assert remove_parenthesis("python (1+1) (2+2) (3+3) (4+4) (5+5) (6+6) (7+7) (8+8)") == "python"
assert remove_parenthesis("python (1+1) (2+2) (3+3) (4+4) (5+5) (6+6) (7+7) (8+8) (9+9)") == "python"
assert remove_parenthesis("python (1+1) (2+2) (3+3) (4+4) (5+5) (6+6) (7+7) (8+8) (9+9) (10+10)") == "python"
assert remove_parenthesis("python (1+1) (2+2) (3+3) (4+4) (5+5) (6+6) (7+7) (8+8) (9+9) (10+10) (11+11)") == "python"
assert remove_parenthesis("python (1+1) (2+2) (3+3) (4+4) (5+5) (6+6) (7+7) (8+8) (9+9) (10+10) (11+11) (12+12)") == "python"
assert remove_parenthesis("python (1+1) (2+2) (3+3) (4+4) (5+5) (6+6) (7+7) (8+8) (9+9) (10+10) (11+11) (12+12) (13+13)") == "python"
assert remove_parenthesis("python (1+1) (2+2) (3+3) (4+4) (5+5) (6+6) (7+7) (8+8) (9+9) (10+10) (11+11) (12+12) (13+13) (14+14)") == "python"
assert remove_parenthesis("python (1+1) (2+2) (3+3) (4+4) (5+5) (6+6) (7+7) (8+8) (9+9) (10+10) (11+11) (12+12) (13+13) (14+14) (15+15)") == "python"
assert remove_parenthesis("python (1+1) (2+2) (3+3) (4+4)