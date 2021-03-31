# Question 1
"""
2^10            = O(1)
2 log(n)        = O(log(n))
3n + 100 log(n) = O(n)
4n              = O(n)
n log(n)        = O(n log(n))
4n log(n) + 2n  = O(n log(n))
n^2 + 10n       = O(n^2)
n^3             = O(n^3)
2^n             = O(2^n)
"""

# Question 2
"""
A(n) = 8n log(n)
B(n) = 2n^2

Simplified...
A(n) = 4 log(n)
B(n) = n

let A = B
4 log(n) = n
log(n^4) = n
2^n = n^4

Because the provided values are both powers of 2 and both are simple x^y power expressions, I'm expecting my n value to be a power of 2 as well.

let n = 2
2^2 < 2^4

let n = 4
2^4 < 4^4

let n = 8
2^8 < 4^4

let n = 16
2^16 = 16^4

Therefore, algoritm A is faster when n is greater than 16
"""

# Question 3
# This one I had to look at the solutions to figure out.
"""
d(n) = O(f(n))

d(n) <= c f(n) where n >= n₀
a d(n) <= ac f(n) where n >= n₀

let c₂ = ac
a d(n) <= c₂ f(n) where n >= n₀

Therefore, a d(n) = O(f(n))
"""

# Question 4
# 1
def example1(S):
    n = len(S)
    total = 0
    for j in range(n):
        total += S[j]
    return total
"""
= O(n)
"""

# 2
def example2(S):
    n = len(S)
    total = 0
    for j in range(0, n, 2):
        total += S[j]
    return total
"""
= O(n)
"""

# 3
def example3(S):
    n = len(S)
    total = 0
    for j in range(n):
        for k in range(1 + j):
            total += S[k]
    return total
"""
= O(n^2)
"""

# 4
def example4(S):
    n = len(S)
    prefix = 0
    total = 0
    for j in range(n):
        prefix += S[j]
        total += prefix
    return total
"""
= O(n)
"""

# 5
def example5(A, B):
    n = len(A)
    count = 0
    for i in range(n):
        total = 0
        for j in range(n):
            for k in range(1 + j):
                total += A[k]
        if B[i] == total:
            count += 1
"""
= O(n^3)
"""