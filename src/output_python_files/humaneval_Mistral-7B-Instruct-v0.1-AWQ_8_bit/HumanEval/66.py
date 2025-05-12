def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    sum = 0
    for c in s:
        if c.isalpha():
            continue
        sum += ord(c)
    return sum


def main():
    for s in ["", "abAB", "abcCd", "helloE", "woArBld", "aAaaaXa"]:
        print(digitSum(s))


if __name__ == '__main__':
    main()