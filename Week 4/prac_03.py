# Question 1
def maxElement(S, i):
    # If last element of S
    if i == len(S)-1:
        return S[i]
    
    max = maxElement(S, i+1)
    if S[i] > max:
        return S[i]
    else:
        return max

print(maxElement([16, 2, 3, 5, 4, -10, 5, 1], 0))
"""
Input: array (S), index (i)
Output: Largest number of S

Run time = O(n)
"""

# Question 2
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)
print(power(2, 5))
"""
power(2, 5)      return 2 * 16 = 32
        V                   ^
power(2, 4)      return 2 * 8 = 16
        V                   ^
power(2, 3)      return 2 * 4 = 8
        V                   ^
power(2, 2)      return 2 * 2 = 4
        V                   ^
power(2, 1)      return 2 * 1 = 2
        V                   ^
power(2, 0)  ->  return 1
"""

# Question 3
def power2(x, n):
    if n == 0:
        return 1
    else:
        partial = power2(x, n // 2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result
print(power2(2, 18))
"""
power2(2, 18)     return 2 * 16 = 32
        V                ^
power2(2, 9)      return (16 * 16) * 2 = 16
        V                 ^    ^
power2(2, 4)      return 2 * 4 = 8
        V                ^
power2(2, 2)      return 2 * 2 = 4
        V                ^
power2(2, 1)      return (1 * 1) * 2 = 2
        V                 ^   ^
power2(2, 0)  ->  return 1
"""

# Question 4
def product(m, n):
    if n == 1:
        return m
    else:
        return m + product(m, n - 1)
print(product(3, 6))
"""
Multiplication is done by adding a number to iself the given
amount of times, e.g. 4 x 4 = 4 + 4 + 4 + 4. This means to
make a recursive algoritm for the product of two numbers, it
will need to recur by n then reduce n by 1 until it reaches 1.
"""

# Question 5
import sys
from time import time
from dynamic_array import DynamicArray

try:
    maxN = int(sys.argv[1])
except:
    maxN = 10000000

def compute_average(n):
    """Perform n appends to an empty list and return average time elapsed."""
    data = DynamicArray()
    start = time()                 # record the start time (in seconds)
    for k in range(n):
        data.append(None)
    end = time()                   # record the end time (in seconds)
    return (end - start) / n       # compute average per operation

n = 10
while n <= maxN:
  print('Average of {0:.3f} for n {1}'.format(compute_average(n)*1000000, n))
  n *= 10
"""
When using the normal Python list, I got this output:
    Average of 0.000 for n 10
    Average of 0.000 for n 100
    Average of 0.999 for n 1000
    Average of 0.101 for n 10000
    Average of 0.110 for n 100000
    Average of 0.096 for n 10000000

When using DyanmicArray, I got this output:
    Average of 0.000 for n 10
    Average of 0.000 for n 100
    Average of 0.000 for n 1000
    Average of 0.601 for n 10000
    Average of 0.499 for n 100000
    Average of 0.726 for n 1000000
    Average of 0.509 for n 10000000

This shows the normal Python list is much faster than DynamicArray.
"""

# Question 6
class DynamicArrayResize(DynamicArray):
    def __init__(self, resize_factor):
        super().__init__()
        self._resize_factor = resize_factor
    
    def append(self, obj):
        if self._n == self._capacity:
            self._resize(int(self._resize_factor * self._capacity) + 1)
        self._A[self._n] = obj
        self._n += 1

try:
    maxN = int(sys.argv[1])
except:
    maxN = 10000000

def compute_average2(n):
    """Perform n appends to an empty list and return average time elapsed."""
    data = DynamicArrayResize(32)
    start = time()                 # record the start time (in seconds)
    for k in range(n):
        data.append(None)
    end = time()                   # record the end time (in seconds)
    return (end - start) / n       # compute average per operation

n = 10
while n <= maxN:
    print('Average of {0:.3f} for n {1}'.format(compute_average2(n)*1000000, n))
    n *= 10
"""
With a resize factor of 1.5, I got this result:
    Average of 0.000 for n 10
    Average of 0.000 for n 100
    Average of 3.005 for n 1000
    Average of 3.492 for n 10000
    Average of 2.290 for n 100000
    Average of 2.275 for n 1000000
    Average of 1.563 for n 10000000

With a resize factor of 4, I got this result:
    Average of 0.000 for n 10
    Average of 0.000 for n 100
    Average of 0.998 for n 1000
    Average of 0.403 for n 10000
    Average of 0.569 for n 100000
    Average of 0.368 for n 1000000
    Average of 0.394 for n 10000000

It seems like the greater the resize factor, the faster the operation.
"""