# Question 1
def is_multiple(n, m):
    return True if m % n == 0 else False
print(is_multiple(2, 6))

# Question 2
print([2**i for i in range(9)])

# Question 3
def are_distinct(array):
    for index, value in enumerate(array):
        for key in range(index+1, len(array)):
            if array[key] == value:
                return False
    return True
print(are_distinct([1, 2, 3, 4, 5]))

# Question 4
def harmonic_gen(n):
    value = 0
    denominator = 1
    while denominator <= n:
        value += 1/denominator
        denominator += 1
        yield value

for value in harmonic_gen(10):
    print(value)
    break