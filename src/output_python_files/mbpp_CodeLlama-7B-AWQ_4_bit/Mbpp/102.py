"""
Write a function to convert a snake case string to camel case string.
assert snake_to_camel('python_program')=='PythonProgram'
"""


def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


if __name__ == '__main__':
    print(snake_to_camel('python_program'))
    print(snake_to_camel('python_program_is_fun'))
    print(snake_to_camel('python_program_is_fun_and_easy'))
    print(snake_to_camel('python_program_is_fun_and_easy_to_use'))
    print(snake_to_camel('python_program_is_fun_and_easy_to_use_and_readable'))
    print(snake_to_camel('python_program_is_fun_and_easy_to_use_and_readable_by_humans'))
    print(snake_to_camel('python_program_is_fun_and_easy_to_use_and_readable_by_humans_and_machines'))
    print(snake_to_camel('python_program_is_fun_and_easy_to_use_and_readable_by_humans_and_machines_and_robots'))
    print(snake_to_camel('python_program_is_fun_and_easy_to_use_and_readable_by_humans_and_machines_and_robots_and_dogs'))
    print(snake_to_camel('python_program_is_fun_and_easy_to_use_and_readable_by_humans_and_machines_and_robots_and_dogs_and_cats'))
    print(snake_to_camel('python_program_is_fun_and_easy_to_use_and_readable_by_humans_and_machines_and_robots_and_dogs_and_cats_and_monkeys'))
    print(snake_to_camel('python_program_is_fun_and_easy_to_use_and_readable_by_humans_and_machines_and_robots_and_dogs_and_cats_and_monkeys_and_elephants'))
    print(snake_to_camel('python_program_is_fun_and_easy_to_use_and_readable_by_humans_and_machines_and_robots_and_dogs_and_cats_and_monkeys_and_elephants_and_giraffes'))
    print(snake_to_camel('python_program_is_fun_and_easy_to_use_and_readable_by_humans_and_machines_and_robots_and_dogs_and_cats_and_monkeys_and_elephants_and_giraffes_and_lions'))
    print(snake_to_camel('python_program_is_fun_and_easy_to_use_and_readable_by_humans_and_machines_and_robots_and_dogs_and_cats_and_monkeys_and_elephants_and_giraffes_and_lions_and_tigers'))
    print(snake_to_camel('python_program_is_fun_and_easy_to_use_and_readable_by_humans_and_machines_and_robots_and_dogs_and_cats_and_monkeys_and_elephants_and_giraffes_and_lions_and_tigers_and_bears'))
    print(snake_to_camel('python_program_is_fun_and_easy