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
    # replace all spaces with underscores
    text = text.replace(" ", "_")

    # replace more than 2 consecutive spaces with -
    text = text.replace("_ _", "-")
    text = text.replace("_ _ _", "- - -")
    text = text.replace("_ _ _ _", "- - - -")
    text = text.replace("_ _ _ _ _", "- - - - -")

    return text


def test_fix_spaces():
    """
    Test fix_spaces function
    """
    assert fix_spaces("Example") == "Example"
    assert fix_spaces("Example 1") == "Example_1"
    assert fix_spaces(" Example 2") == "_Example_2"
    assert fix_spaces(" Example   3") == "_Example-3"
    assert fix_spaces(" Example      4") == "_Example--4"
    assert fix_spaces(" Example    12345") == "_Example-12345"
    assert fix_spaces(" Example 123 456") == "_Example-123_456"
    assert fix_spaces(" Example 123 456 789") == "_Example-123_456_789"
    assert fix_spaces(" Example 123 456 789 1011") == "_Example-123_456_789_1011"
    assert fix_spaces(" Example 123 456 789 1011 123456789") == "_Example-123_456_789_1011_123456789"


if __name__ == "__main__":
    test_fix_spaces()