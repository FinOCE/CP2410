# Question 1
def find_second_last_node(L):
    if L.head is None or L.head.next is None:
        return None
    current = L.head
    next = L.head.next
    while next.next is not None:
        current = next
        next = next.next
    return current

# Question 2
def count_nodes(L):
    if L.current is None:
        return 0
    count = 1
    original = L.current
    current = original
    while current.next != original:
        count += 1
        current = current.next
    return count

# Question 3
def in_same_circular_list(x, y):
    current = x
    while current.next is not y:
        if current.next is x:
            return False
        current = current.next
    return True

# Question 4
from positional_list import PositionalList

def list_to_positional_list(L):
    positional_list = PositionalList()
    for prop in L:
        positional_list.add_last(prop)
    return pos_L

# Question 5
def max(self):
    return max(prop for prop in self)