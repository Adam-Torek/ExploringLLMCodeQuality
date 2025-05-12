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
    letter_grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E']
    grades = sorted(grades)
    result = []
    for grade in grades:
        if grade >= 4.0:
            result.append(letter_grades[0])
        elif grade >= 3.7:
            result.append(letter_grades[1])
        elif grade >= 3.3:
            result.append(letter_grades[2])
        elif grade >= 3.0:
            result.append(letter_grades[3])
        elif grade >= 2.7:
            result.append(letter_grades[4])
        elif grade >= 2.3:
            result.append(letter_grades[5])
        elif grade >= 2.0:
            result.append(letter_grades[6])
        elif grade >= 1.7:
            result.append(letter_grades[7])
        elif grade >= 1.3:
            result.append(letter_grades[8])
        elif grade >= 1.0:
            result.append(letter_grades[9])
        else:
            result.append(letter_grades[10])
    return result


grades = [4.0, 3, 1.7, 2, 3.5]
print(numerical_letter_grade(grades))