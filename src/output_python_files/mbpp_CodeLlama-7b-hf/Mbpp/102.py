"""
Write a function to convert a snake case string to camel case string.
assert snake_to_camel('python_program')=='PythonProgram'
"""


def snake_to_camel(snake_str):
    """
    :param snake_str:
    :return:
    """
    components = snake_str.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + ''.join(x.title() for x in components[1:])


if __name__ == '__main__':
    print(snake_to_camel('python_program'))
    print(snake_to_camel('python_program_is_fun'))
    print(snake_to_camel('python_program_is_fun_to_write'))
    print(snake_to_camel('python_program_is_fun_to_write_and_read'))
    print(snake_to_camel('python_program_is_fun_to_write_and_read_and_debug'))
    print(snake_to_camel('python_program_is_fun_to_write_and_read_and_debug_and_run'))
    print(snake_to_camel('python_program_is_fun_to_write_and_read_and_debug_and_run_and_deploy'))
    print(snake_to_camel('python_program_is_fun_to_write_and_read_and_debug_and_run_and_deploy_and_test'))
    print(snake_to_camel('python_program_is_fun_to_write_and_read_and_debug_and_run_and_deploy_and_test_and_release'))
    print(snake_to_camel('python_program_is_fun_to_write_and_read_and_debug_and_run_and_deploy_and_test_and_release_and_maintain'))
    print(snake_to_camel('python_program_is_fun_to_write_and_read_and_debug_and_run_and_deploy_and_test_and_release_and_maintain_and_improve'))
    print(snake_to_camel('python_program_is_fun_to_write_and_read_and_debug_and_run_and_deploy_and_test_and_release_and_maintain_and_improve_and_enhance'))
    print(snake_to_camel('python_program_is_fun_to_write_and_read_and_debug_and_run_and_deploy_and_test_and_release_and_maintain_and_improve_and_enhance_and_optimize'))
    print(snake_to_camel('python_program_is_fun_to_write_and_read_and_debug_and_run_and_deploy_and_test_and_release_and_maintain_and_improve_and_enhance_and_optimize_and_fix'))
    print(snake_to_camel('python_program_is_fun_to_write_and_read_and_debug_and_run_and_deploy_and_test_and_release_and_maintain_and_improve_and_enhance_and_optimize_and_fix_and_refactor'))
    print(snake_to_camel('python_program_is_fun_to_write_and_read_and_debug_and_run_and_deploy_and_test_and_release_and_maintain_and_improve_and_enhance_and_optimize_and_fix_and_refactor_and_clean'))
    print(snake_to_camel('python_program_is_fun_to_write_and_read_and_debug_and_run_and_deploy_and_test_and_release_and_maintain_and_improve_and_enhance_and_optimize_and_fix_and_refactor_and_clean_and_reuse