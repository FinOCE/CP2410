# Question 1
"""
push(5)     5
push(3)     5, 3
pop()       5 return 3
push(2)     5, 2
push(8)     5, 2, 8
pop()       5, 2 return 8
pop()       5 return 2
push(9)     5, 9
push(1)     5, 9, 1
pop()       5, 9 return 1
push(7)     5, 9, 7
push(6)     5, 9, 7, 6
pop()       5, 9, 7 return 6
pop()       5, 9 return 7
push(4)     5, 9, 4
pop()       5, 9 return 4
pop()       5 return 9
"""

# Question 2
"""
With 25 push operations executed and 10 pop, where 3 failed, that makes 25 - (10 - 3) = 18
"""

# Question 3
from array_stack import ArrayStack

def transfer(S, T):
    while not S.is_empty():
        T.push(S.pop())

S = ArrayStack()
S.push(1)
S.push(2)
S.push(3)
S.push(4)
S.push(5)
T = ArrayStack()

print(S._data, T._data)
transfer(S, T)
print(S._data, T._data)

# Question 4
"""
enqueue(5)  5
enqueue(3)  5, 3
dequeue()   5 return 3
enqueue(2)  5, 2
enqueue(8)  5, 2, 8
dequeue()   5, 2 return 8
dequeue()   5 return 2
enqueue(9)  5, 9
enqueue(1)  5, 9, 1
dequeue()   5, 9 return 1
enqueue(7)  5, 9, 7
enqueue(6)  5, 9, 7, 6
dequeue()   5, 9, 7 return 6
dequeue()   5, 9 return 7
enqueue(4)  5, 9, 4
dequeue()   5, 9 return 4
dequeue()   5 return 9
"""

# Question 5
"""
With 32 enqueue operations executed and 15 dequeue, where 5 failed, that makes 32 - (15 - 5) = 22
"""

# Question 6
from array_queue import ArrayQueue

def transferQueue(D, Q):
    while not D.is_empty():
        Q.enqueue(D.dequeue())

D = ArrayQueue()
D.enqueue(1)
D.enqueue(2)
D.enqueue(3)
D.enqueue(4)
D.enqueue(5)
D.enqueue(6)
D.enqueue(7)
D.enqueue(8)
Q = ArrayQueue()

print(D._data, Q._data)
transferQueue(D, Q)
print(D._data, Q._data)

# Question 7
def transferQueueToStack(D, S):
    while not D.is_empty():
        S.push(D.dequeue())
D = ArrayQueue()
D.enqueue(1)
D.enqueue(2)
D.enqueue(3)
D.enqueue(4)
D.enqueue(5)
D.enqueue(6)
D.enqueue(7)
D.enqueue(8)
S = ArrayStack()

print(D._data, S._data)
transferQueueToStack(D, S)
print(D._data, S._data)