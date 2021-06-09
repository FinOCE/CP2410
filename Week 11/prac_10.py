# Question 1
"""
Merge-sort has a time complexity of O(n log n), because the height of the tree is log n, and at each node of the tree needs to run for time n.

The quick-sort algorithm uses a random element as a pivot to partition the sequence by, so because there are only the possible values of 0 and 1 in a bit, it would only take one iteration to sort, therefore taking O(n) time.
"""

# Question 2
"""
Merging the two sorted sequences takes O(n) time and can then use a linear scan to remove any duplicates in the new sequence.
"""

# Question 3
"""
Because the possible values are 0 and 1 again like question 1, the quick-sort algorithm can once again use one of the values as the pivot, therefore only taking 1 interation to sort the set, taking O(n) time.
"""

# Question 4
"""
By first sorting the sequence, each of the candidate's votes will be grouped together in the sequence. With this, an algorithm can be used to count how many of a vote there is, and compare it to the previously most voted candidate. By the end of the linear scan, the candidate with the most votes is returned, regardless of the number of candidates, and would take O(n log n) time.
"""

# Question 5
"""
If there was a small number of candidates, the counts of votes can be stored in an array of equal length to the number of candidates, where each cell represents a candidate. With this, the sequence can be iterated through, adding to the array at the key representing each candidate, taking O(n) time. Once this is done, the array value with the greatest number's key represents the winner of the vote.
"""

# Question 6
"""
        1000 80 10 50 70 60 90 20
  1000 80 10 50            70 60 90 20
1000 80     10 50       70 60       90 20
80 1000     10 50       60 70       20 90
  10 50 80 1000            20 60 70 90
        10 20 50 60 70 80 90 1000
"""