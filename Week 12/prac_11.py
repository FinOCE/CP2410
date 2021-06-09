# Question 1
"""
Adjacency list

U -> (V, W)
V -> (U, W, X)
W -> (U, V, X, Y)
X -> (V, W, Y, Z)
Y -> (W, X)
Z -> (x)

Adjacency matrix

  U  V  W  X  Y  Z
U 0  1  1  0  0  0
V 1  0  1  1  0  0
W 1  1  0  1  1  0
X 0  1  1  0  1  1
Y 0  0  1  1  0  0
Z 0  0  0  1  0  0
"""

# Question 2
"""
Z

Z -> X
All Z edges visited

Z -> X -> Y
          W
          Y
All X edges visited

Z -> X -> Y
          W -> U
          Y
All V edges visited, then in order W, Y, U

There isn't really a good way to show these diagrams in text.
"""

# Question 3
"""
U

U -> V

U -> V
       -> W

u -> V      -> X
       -> W

u -> V      -> X
       -> W      -> Y

Y = 5/6

u -> V      -> X      -> Z
       -> W      -> Y

Z = 7/8
X = 4/9
W = 3/10
V = 2/11
U = 1/12
"""

# Question 4
# a
"""
1 - 2
| X |
4 - 3
|
6 - 5
| / |
7 - 8
"""

# b
"""
1

1 -> 2
     3
     4
All of 1 visited, then 2, then 3

1 -> 2
     3
     4 -> 6
All of 4 visited
    
1 -> 2
     3
     4 -> 6 -> 5
               7
All of 6 visited

1 -> 2
     3
     4 -> 6 -> 5 -> 8
               7
All of 5 visited, then 7, then 8
"""

# c
"""
1

1 -> 2

1 -> 2
       -> 3

1 -> 2
       -> 3
            -> 4

1 -> 2
       -> 3
            -> 4 -> 6

1 -> 2
       -> 3
            -> 4 -> 6 -> 5

1 -> 2
       -> 3
            -> 4 -> 6 -> 5 -> 7

1 -> 2
       -> 3
            -> 4 -> 6 -> 5 -> 7 -> 8

8 = 8/9
7 = 7/10
5 = 6/11
6 = 5/12
4 = 4/13
3 = 3/14
2 = 2/15
1 = 1/16
"""