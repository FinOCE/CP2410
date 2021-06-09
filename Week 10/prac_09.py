# Question 1
"""
30, 40, 24, 58, 48, 26, 25

Insert 30
    30
-       -

Insert 40
        30
-               40
            -       -

Insert 24
            30
    24              40
-       -       -       -

Insert 58
                30
    24                  40
-       -           -           58
                            -       -

Insert 48
                30
    24                  40
-       -       -                   58
                            48              -
                        -       -

Insert 26
                30
    24                  40
-       26                         58
    -       -               48              -
                        -       -

Insert 25
                30
    24                      40
-           26                          58
        25       -               48              -
    -        -               -       -
"""

# Question 2
"""
Tree 1
        1
-               2
            -       3

Tree 2
            3
    2           -
1       -

Tree 3
        1
-               3
            2       -

Tree 4
            3
    1               -
-       2

Tree 5
    2
1       3

There are 5 different binary search trees that can store the keys {1, 2, 3}
"""

# Question 3
"""
I won't add the external nodes because they make it quite a bit more difficult to write, but they would be there for the AVL tree.

                        62
        44                              78
17              50                              88
            48      54

Insert 52
                            62
            50                              78
    17              54                              88
17      48      52
"""

# Question 4
"""
K = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

                  4 8 12

1 2 3       5 6 7       9 10 11     13 14 15
- - - -     - - - -     - - - -     - - - -
"""

# Question 5
"""
5, 16, 22, 45, 2, 10, 18, 30, 50, 12, 1

Insert 5
5

Insert 16
5 16

Insert 22
5 16 22

Insert 45
       22

5 16        45

Insert 2

         22

2 5 16        45

Insert 10
        10 22

2 5     16          45

Insert 18
        10 22

2 5     16 18       45

Insert 30
        10 22

2 5     16 18       30 45

Insert 50
        10 22

2 5     16 18       30 45 50

Insert 12
        10 12 22

2 5     16 18       30 45 50

Insert 1
        10 22

1 2 5   12 16 18    30 45 50
"""

# Question 6
"""
10, 16, 12, 14, 13

Insert 10
10

Insert 16
    10
-       16

    16
-       10

Insert 12
            16
    10              -
-       12

    12
10      16

Insert 14
            12
    10              16
                14      -

            14
    12              16
10      -

Insert 13
            14
    12              16
10      13

            13
    12              14
10      -       -       16
"""