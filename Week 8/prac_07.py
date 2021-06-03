# Question 1
# a
"""
5
5, 6
3, 5, 6
1, 3, 5, 6
1, 2, 3, 5, 6
1, 2, 3, 5, 6, 7
1, 2, 3, 5, 6, 7, 9
1, 2, 3, 5, 6, 7, 8, 9
"""

# b
"""
5, 6, 3, 1, 2, 7, 9, 8
1, 6, 3, 5, 2, 7, 9, 8
1, 2, 3, 5, 6, 7, 9, 8
1, 2, 3, 5, 6, 7, 9, 8
1, 2, 3, 5, 6, 7, 9, 8
1, 2, 3, 5, 6, 7, 8, 9
1, 2, 3, 5, 6, 7, 8, 9
"""

# Question 2
"""
5, 4, 3, 2, 1
5               No shifts
4, 5            1 shift
3, 4, 5         2 shift
2, 3, 4, 5      3 shift
1, 2, 3, 4, 5   4 shift

By making the initial values insert in order of greatest to smallest,
The following insertion will require n+1 shifts, therefore making it
take O(n^2) time.
"""

# Question 3
"""
5

    5
1

    1
5

    1
5       4

            1
    5               4
7

            1
    5               4
7       3

            1
    3               4
7       5

            1
    3               4
7       5       9

            1
    3               4
7       5       9       0

            1
    3               0
7       5       9       4

            0
    3               1
7       5       9       4

                0
        3               1
    7       5       9       4
2

                0
        3               1
    2       5       9       4
7

                0
        2               1
    3       5       9       4
7

                            0
            2                               1
    3               5               9               4
7       8
"""

# Question 4
"""
            2
    3               4
8       5       7       6

            6
    3               4
8       5       7

            4
    3               6
8       5       7

            3
    4               6
8       5       7
"""

# Question 5
"""
The third-smallest key would be stored in the depth of 2,
since the smallest would be at the top and second smallest
shared position in depth = 2.
"""

# Question 6
"""
The largest key would be stored in any external node as it
cannot have any children.
"""