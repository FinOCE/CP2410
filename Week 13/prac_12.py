# Question 1
"""
Adjacency list

A -> B, C, D
B -> D
C -> D, E
D -> E
E -> A

Adjacency matrix

  A  B  C  D  E
A 0  1  1  1  0
B 0  0  0  1  0
C 0  0  0  1  1
D 0  0  0  0  1
E 1  0  0  0  0
"""

# Question 2
"""
   -->   -->   -->
 A     B     C     D     
   <--   <--   <--
^ |               | ^
| v               v |
   <--   <--   <--
 H     G     F     E
   -->   -->   -->

An example of a non-simple Euler tour on this graph is:
A -> B -> C -> D -> E -> F -> G -> H -> A -> H -> G -> F -> E -> D -> C -> B -> A
"""

# Question 3
"""
A

A -> B

A -> B
  -> D

A -> B
  -> D
  -> C

A -> B -> E
  -> D
  -> C

A -> B -> E -> F
  -> D
  -> C
"""

# Question 4
# a
"""
A B C D E F

A B C D E-F

A B C-D E-F

A C-D-B E-F

A B-D-F-E
    |
    C

A-B-D-F-E
    |
    C
"""

# b
"""
A B C D E F

A-B C D E F

A-B-D C E F

A-B-D-C E F

A-B-D-F E
    |
    C

A-B-D-F-E
    |
    C
"""