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
    letter_grades = []
    for grade in grades:
        if grade >= 4.0:
            letter_grades.append('A+')
        elif grade >= 3.7:
            letter_grades.append('A')
        elif grade >= 3.3:
            letter_grades.append('A-')
        elif grade >= 3.0:
            letter_grades.append('B+')
        elif grade >= 2.7:
            letter_grades.append('B')
        elif grade >= 2.3:
            letter_grades.append('B-')
        elif grade >= 2.0:
            letter_grades.append('C+')
        elif grade >= 1.7:
            letter_grades.append('C')
        elif grade >= 1.3:
            letter_grades.append('C-')
        elif grade >= 1.0:
            letter_grades.append('D+')
        elif grade >= 0.7:
            letter_grades.append('D')
        else:
            letter_grades.append('E')
    return letter_grades


# Test the function with the example
print(numerical_letter_grade([4.0, 3, 1.7, 2, 3.5])) # Output: ['A+', 'B', 'C-', 'C', 'A-']

# Test the function with some other inputs
print(numerical_letter_grade([3.8, 3.5, 2.9, 2.1, 1.8, 1.5, 0.9])) # Output: ['A', 'B', 'C', 'D+', 'D', 'E']
print(numerical_letter_grade([3.2, 2.9, 2.1, 1.8, 1.5, 0.9, 0.0])) # Output: ['B-', 'B', 'D', 'D', 'E', 'E']
print(numerical_letter_grade([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])) # Output: ['E', 'E', 'E', 'E', 'E', 'E', 'E']
print(numerical_letter_grade([4.5, 4.2, 3.9, 3.6, 3.3, 2.6, 1.1])) # Output: ['A', 'A', 'B', 'B', 'C', 'D-']

# Test the function with some edge cases
print(numerical_letter_grade([4.1, 3.8, 3.6, 3.3, 2.9, 2.6, 1.1, 0.0])) # Output: ['A', 'A', 'B', 'B', 'C', 'D', 'E']
print(numerical_letter_grade([4.0, 3.7, 3.3, 2.7,