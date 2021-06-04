# Question 1
"""
h(i) = (3i + 5) mod 11

h(12) = 8
h(44) = 5
h(13) = 0
h(88) = 5
h(23) = 8
h(94) = 1
h(11) = 5
h(39) = 1
h(20) = 10
h(16) = 9
h(5) = 9

0   1   2   3   4   5   6   7   8   9   10
--------------------------------------------
13  94              44          12  16  20
    39              88          23  5
                    11
"""

# Question 2
"""
0   1   2   3   4   5   6   7   8   9   10
--------------------------------------------
13  94  39  16  5   44  88  11  12  23  20
"""

# Question 3
"""
h(i) = ((3i + 5) + j^2) mod 11    for j = 0, 1, ...

h(12) = 8
h(44) = 5
h(13) = 0
h(88) = 6   j = 1
h(23) = 9   j = 1
h(94) = 1
h(11) =23   j = 3
h(39) = 1   j = 1
h(20) = 10
h(16) = 7   j = 3
h(5) = ?    cannot load

h(5) cannot be loaded because ((3*5 + 5) + j^2) mod 11
never fits an open key (4) in the hash table.

0   1   2   3   4   5   6   7   8   9   10
--------------------------------------------
13  94  39  11      44  88  16  12  23  20
"""

# Question 4
"""
h(i) = ((3i + 5) + j*(7 - (k mod 7))) mod 11

h(12) = 8   j = 0
h(44) = 5   j = 0
h(13) = 0   j = 0
h(88) = 3   j = 3
h(23) = 2   j = 1
h(94) = 6   j = 1
h(11) = 9   j = 1
h(39) = 1   j = 0
h(20) = 10  j = 0
h(16) = 7   j = 4
h(5) = 4    j = 3

0   1   2   3   4   5   6   7   8   9   10
--------------------------------------------
13  39  23  88  5   44  94  16  12  11  20
"""

# Question 5
"""
h(k) = 3k mod 17

h(54) = 9
h(28) = 16
h(41) = 4
h(18) = 3
h(10) = 13
h(36) = 6
h(25) = 7
h(38) = 12
h(12) = 2
h(90) = 15

0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19
--------------------------------------------------------------------------------
        12  18  41      36  25      54          38  10      90  28
"""

# Question 6
"""
By using a binary search algorithm, we can find the position of the first 0 for
each row. Once we find the position of this first 0, all the cellsto the left
would be 1, therefore they can be added together.

This solution would take O(n log n) time to complete as the binary search agorithm
is a O(log n) algorithm and it needs to run for every row in the n*n array.
"""