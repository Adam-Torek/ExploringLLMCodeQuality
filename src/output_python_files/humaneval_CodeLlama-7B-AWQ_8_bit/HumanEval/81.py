def numerical_letter_grade(grades):
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E
    

    Example:
    grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    """
    # Your code here
    return [letter_grade(gpa) for gpa in grades]


def letter_grade(gpa):
    """
    This function takes in a gpa and returns the corresponding letter grade.
    """
    if gpa >= 4.0:
        return 'A+'
    elif gpa >= 3.7:
        return 'A'
    elif gpa >= 3.3:
        return 'A-'
    elif gpa >= 3.0:
        return 'B+'
    elif gpa >= 2.7:
        return 'B'
    elif gpa >= 2.3:
        return 'B-'
    elif gpa >= 2.0:
        return 'C+'
    elif gpa >= 1.7:
        return 'C'
    elif gpa >= 1.3:
        return 'C-'
    elif gpa >= 1.0:
        return 'D+'
    elif gpa >= 0.7:
        return 'D'
    elif gpa >= 0.0:
        return 'D-'
    else:
        return 'E'


def numerical_letter_grade_2(grades):
    """
    This function takes in a list of GPAs and returns a list of corresponding letter grades.
    """
    return [letter_grade(gpa) for gpa in grades]


def letter_grade_2(gpa):
    """
    This function takes in a gpa and returns the corresponding letter grade.
    """
    if gpa >= 4.0:
        return 'A+'
    elif gpa >= 3.7:
        return 'A'
    elif gpa >= 3.3:
        return 'A-'
    elif gpa >= 3.0:
        return 'B+'
    elif gpa >= 2.7:
        return 'B'
    elif gpa >= 2.3:
        return 'B-'
    elif gpa >= 2.0:
        return 'C+'
    elif gpa >= 1.7:
        return 'C'
    elif gpa >= 1.3:
        return 'C-'
    elif gpa >= 1.0:
        return 'D+'
    elif gpa >= 0.7:
        return 'D'
    elif gpa >= 0.0:
        return 'D-'
    else:
        return 'E'


def numerical_letter_grade_3(grades):
    """
    This function takes in a list of GPAs and returns a list of corresponding letter grades.
    """
    return [letter_grade_3(gpa) for gpa in grades]


def letter_grade_3(gpa):
    """
    This function takes in a gpa and returns the corresponding letter grade.
    """
    if gpa >= 4.0:
        return 'A+'
    elif gpa >= 3.7:
        return 'A'
    elif gpa >=