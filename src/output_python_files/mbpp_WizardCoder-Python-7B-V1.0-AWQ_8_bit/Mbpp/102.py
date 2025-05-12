"""
Write a function to convert a snake case string to camel case string.
assert snake_to_camel('python_program')=='PythonProgram'
"""

def snake_to_camel(snake_str):
    words = snake_str.split('_')
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])

# Test cases
print(snake_to_camel('python_program')) # Output: PythonProgram
print(snake_to_camel('snake_case_string_to_camel_case_string')) # Output: SnakeCaseStringToCamelCaseString
print(snake_to_camel('snake_case_string_to_camel_case_string_function')) # Output: SnakeCaseStringToCamelCaseStringFunction
print(snake_to_camel('snake_case_string_to_camel_case_string_function_to_test')) # Output: SnakeCaseStringToCamelCaseStringFunctionToTest

# Additional test cases
print(snake_to_camel('snake_case_string_to_camel_case_string_function_to_test_123')) # Output: SnakeCaseStringToCamelCaseStringFunctionToTest123
print(snake_to_camel('snake_case_string_to_camel_case_string_function_to_test_123_abc')) # Output: SnakeCaseStringToCamelCaseStringFunctionToTest123Abc
print(snake_to_camel('snake_case_string_to_camel_case_string_function_to_test_123_abc_def')) # Output: SnakeCaseStringToCamelCaseStringFunctionToTest123AbcDef
print(snake_to_camel('snake_case_string_to_camel_case_string_function_to_test_123_abc_def_ghi')) # Output: SnakeCaseStringToCamelCaseStringFunctionToTest123AbcDefGhi
print(snake_to_camel('snake_case_string_to_camel_case_string_function_to_test_123_abc_def_ghi_jkl')) # Output: SnakeCaseStringToCamelCaseStringFunctionToTest123AbcDefGhiJkl
print(snake_to_camel('snake_case_string_to_camel_case_string_function_to_test_123_abc_def_ghi_jkl_mno')) # Output: SnakeCaseStringToCamelCaseStringFunctionToTest123AbcDefGhiJklMno
print(snake_to_camel('snake_case_string_to_camel_case_string_function_to_test_123_abc_def_ghi_jkl_mno_pqr')) # Output: SnakeCaseStringToCamelCaseStringFunctionToTest123AbcDefGhiJklMnoPqr
print(snake_to_camel('snake_case_string_to_camel_case_string_function_to_test_123_abc_def_ghi_jkl_mno_pqr_stu')) # Output: SnakeCaseStringToCamelCaseStringFunctionToTest123AbcDefGhiJklMnoPqrStu
print(snake_to_camel('snake_case_string_to_camel_case_string_function_to_test_123_abc_def_ghi_jkl_mno_pqr_stu_vw')) # Output: SnakeCaseStringToCamelCaseStringFunctionToTest123AbcDefGhiJklMnoPqrStuVw
print(snake_to_camel('snake_case_string_to_camel_case_string_function_to_test_123_abc_def_ghi_jkl_mno_pqr_stu_vw_xy')) # Output: SnakeCaseStringToCamelCaseStringFunctionToTest123AbcDefGhiJklMnoPqrStuVwXy
print(snake_to_