"""
Write a function that takes in a list of tuples and returns a list containing the rear element of each tuple.
assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
"""

def rear_extract(tuples):
    return [t[2] for t in tuples]


if __name__ == '__main__':
    print(rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]))
    print(rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19), (4, 'Rash', 21), (5, 'Varsha', 20), (6, 'Kil', 19)]))
    print(rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19), (4, 'Rash', 21), (5, 'Varsha', 20), (6, 'Kil', 19), (7, 'Rash', 21), (8, 'Varsha', 20), (9, 'Kil', 19)]))
    print(rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19), (4, 'Rash', 21), (5, 'Varsha', 20), (6, 'Kil', 19), (7, 'Rash', 21), (8, 'Varsha', 20), (9, 'Kil', 19), (10, 'Rash', 21), (11, 'Varsha', 20), (12, 'Kil', 19), (13, 'Rash', 21), (14, 'Varsha', 20), (15, 'Kil', 19), (16, 'Rash', 21), (17, 'Varsha', 20), (18, 'Kil', 19), (19, 'Rash', 21), (20, 'Varsha', 20), (21, 'Kil', 19), (22, 'Rash', 21), (23, 'Varsha', 20), (24, 'Kil', 19), (25, 'Rash', 21), (26, 'Varsha', 20), (27, 'Kil', 19), (28, 'Rash', 21), (29, 'Varsha', 20), (30, 'Kil', 19), (31, 'Rash', 21), (32, 'Varsha', 20), (33, 'Kil', 19), (34, 'Rash', 21), (35, 'Varsha', 20), (36, 'Kil', 19), (37, 'Rash', 21), (38, 'Varsha', 20), (39, 'Kil', 19), (40, 'Rash', 21), (41, 'Varsha', 20), (42, 'Kil', 19), (43, 'Rash', 21), (44, 'Varsha', 20), (45, 'Kil', 19), (46, 'Rash', 21), (47, 'Varsha', 20), (48, 'Kil', 19), (49, 'Rash', 21), (50, 'Varsha', 20), (51, 'Kil', 19), (52, 'Rash', 21), (53, 'Varsha', 20), (54, 'Kil', 19), (55, 'Rash', 21), (56, 'Varsha', 20), (57, '