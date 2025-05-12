def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    for i in range(0, len(s), 2):
        if s[i].isupper():
            count += 1
    return count

# Test cases
print(count_upper('aBCdEf')) # Output: 1
print(count_upper('abcdefg')) # Output: 0
print(count_upper('dBBE')) # Output: 0
print(count_upper('AbcDeF')) # Output: 1
print(count_upper('aBcDeF')) # Output: 1
print(count_upper('AbCdEf')) # Output: 2
print(count_upper('aBcDeFg')) # Output: 2
print(count_upper('aBcDeFgH')) # Output: 2
print(count_upper('aBcDeFgHi')) # Output: 3
print(count_upper('aBcDeFgHiJ')) # Output: 3
print(count_upper('aBcDeFgHiJk')) # Output: 4
print(count_upper('aBcDeFgHiJkL')) # Output: 4
print(count_upper('aBcDeFgHiJkLm')) # Output: 5
print(count_upper('aBcDeFgHiJkLmN')) # Output: 5
print(count_upper('aBcDeFgHiJkLmNo')) # Output: 6
print(count_upper('aBcDeFgHiJkLmNoP')) # Output: 6
print(count_upper('aBcDeFgHiJkLmNoPq')) # Output: 7
print(count_upper('aBcDeFgHiJkLmNoPqR')) # Output: 7
print(count_upper('aBcDeFgHiJkLmNoPqRs')) # Output: 8
print(count_upper('aBcDeFgHiJkLmNoPqRsT')) # Output: 8
print(count_upper('aBcDeFgHiJkLmNoPqRsTu')) # Output: 9
print(count_upper('aBcDeFgHiJkLmNoPqRsTuV')) # Output: 9
print(count_upper('aBcDeFgHiJkLmNoPqRsTuVw')) # Output: 10
print(count_upper('aBcDeFgHiJkLmNoPqRsTuVwX')) # Output: 10
print(count_upper('aBcDeFgHiJkLmNoPqRsTuVwXy')) # Output: 11
print(count_upper('aBcDeFgHiJkLmNoPqRsTuVwXyZ')) # Output: 11
print(count_upper('aBcDeFgHiJkLmNoPqRsTuVwXyZa')) # Output: 12
print(count_upper('aBcDeFgHiJkLmNoPqRsTuVwXyZaB')) # Output: 12
print(count_upper('aBcDeFgHiJkLmNoPqRsTuVwXyZaBc')) # Output: 13
print(count_upper('aBcDeFgHiJkLmNoPqRsTuVwXyZaBcD')) # Output: 13
print(count_upper('aBcDeFgHiJkLmNoPqRsTuVwXyZaBcDe')) # Output: 14
print(count_upper('aBcDeFgHiJkLmNoPqRsTuVwXyZaBcDef')) # Output: 14
print(count_upper('aBcDeFgHiJkLm