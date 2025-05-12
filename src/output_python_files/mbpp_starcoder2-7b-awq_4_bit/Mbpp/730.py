"""
Write a function to remove consecutive duplicates of a given list.
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
"""

def consecutive_duplicates(lst):
    """
    >>> consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
    """
    new_lst = []
    for i in range(len(lst)):
        if lst[i]!= lst[i-1]:
            new_lst.append(lst[i])
    return new_lst

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week_01/day_02/02_01_02_03_04_05_06_07_08_09_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34_35_36_37_38_39_40_41_42_43_44_45_46_47_48_49_50_51_52_53_54_55_56_57_58_59_60_61_62_63_64_65_66_67_68_69_70_71_72_73_74_75_76_77_78_79_80_81_82_83_84_85_86_87_88_89_90_91_92_93_94_95_96_97_98_99_100.py
"""
Write a function that takes a number and returns a list of its digits.
assert digits(1234) == [1, 2, 3, 4]
"""

def digits(number):
    """
    >>> digits(1234)
    [1, 2, 3, 4]
    """
    return [int(i) for i in str(number)]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
/week_01/day_02/02_01_02_03_04_05_06_07_08_09_10_11_12_13_14_15_16_17_18_19_20_21_22_23_24_25_26_27_28_29_30_31_32_33_34_35_36_37_38_39_40_41_42_43_44_45_46_47_48_49_50_51_52_53_54_55_56_57_58_59_60_61_62_63_64_65_66_67_68_69_70_71_72_73_74_75_76_77_78_79_80_81_82_83_84_85_86_87_88_89_90_91_92_93_94_95_96_97_98_99_100.py
"""
Write a function that takes a