"""
Write a function to check if the given number is woodball or not.
assert is_woodall(383) == True
"""
def is_woodball(num):
    """
    Check if the given number is a woodball number or not.
    Woodball numbers are those numbers which can be written as sum of two cubes in two different ways.
    For example: 145 = 8^3 + 7^3 = 17^3 + 16^3
    """
    n = str(num)
    n_len = len(n)
    cube_set = set()

    for i in range(1, int(n**0.5) + 1):
        cube = i**3
        if cube > num:
            break
        if num % cube == 0:
            if (n_len // 2) * 3 > len(cube_set):
                return False
            for j in range(len(cube_set)):
                if cube == cube_set[j] or abs(cube - int(n[j]/3 * 3**3)) < 1:
                    return False
            cube_set.add(cube)

    for i in range(int(n**0.5) + 1, len(n)):
        cube = int(n[i-1:i+1])**3
        if num % cube == 0:
            if (n_len // 2) * 3 > len(cube_set):
                return False
            for j in range(len(cube_set)):
                if cube == cube_set[j] or abs(cube - int(n[j]/3 * 3**3)) < 1:
                    return False
            cube_set.add(cube)

    return True