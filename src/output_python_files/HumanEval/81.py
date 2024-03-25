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
    grade_list = []
    for i in grades:
        if i >= 4.0:
            grade_list.append('A+')
        elif i >= 3.7:
            grade_list.append('A')
        elif i >= 3.3:
            grade_list.append('A-')
        elif i >= 3.0:
            grade_list.append('B+')
        elif i >= 2.7:
            grade_list.append('B')
        elif i >= 2.3:
            grade_list.append('B-')
        elif i >= 2.0:
            grade_list.append('C+')
        elif i >= 1.7:
            grade_list.append('C')
        elif i >= 1.3:
            grade_list.append('C-')
        elif i >= 1.0:
            grade_list.append('D+')
        elif i >= 0.7:
            grade_list.append('D')
        elif i >= 0.0:
            grade_list.append('D-')
        else:
            grade_list.append('E')
    return grade_list


def letter_grade(grade):
    """
    Write a function that takes a number grade (0-100)
    and returns the corresponding letter grade using
    the following scale:

    A 90-100
    B 80-89
    C 70-79
    D 60-69
    F 0-59

    Example:
    letter_grade(95) ==> 'A'
    """
    # Your code here
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'


def letter_grades(grades):
    """
    Write a function that takes a list of test scores
    and returns the letter grades (in the same order)
    using the following scale:

    A 90-100
    B 80-89
    C 70-79
    D 60-69
    F 0-59

    Example:
    letter_grades([95, 92, 80, 50]) ==> ['A', 'A', 'D', 'F']
    """
    # Your code here
    grade_list = []
    for i in grades:
        if i >= 90:
            grade_list.append('A')
        elif i >= 80:
            grade_list.append('B')
        elif i >= 70:
            grade_list.append('C')
        elif i >= 60:
            grade_list.append('D')
        else:
            grade_list.append('F')