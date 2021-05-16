# Setting up data subsets

# Import required modules
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt



# Create function to get all primes required
def get_primes(n):
    """ Finds all prime numbers using Sieve of Eratosthenes based off https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes """
    primes = [False, False, True] + [True for i in range(3, n+1)]
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i**2, n+1, i):
                primes[j] = False
    return primes

"""
The time complexity for the get_primes function is O(n log log n)
"""



# Data Structure 1: DataFrame

# Create Pandas DataFrame with data from CSV and organise
cities = pd.read_csv('cities.csv', low_memory=False)

cities['X'] = pd.to_numeric(cities['X'])
cities['Y'] = pd.to_numeric(cities['Y'])

primes = get_primes(len(cities)-1)
cities['is_prime'] = primes

cities.head(10)

"""
The DataFrame data structure from the pandas library is used to store the data from the CSV. This is used because it is multi-dimensional, allowing it to store data like a spreadsheet would. This allows the properties X, Y, and is_prime to be set to a city efficiently without the need for large dictionaries or combinations of key/value -> object structures. As well as this, the pandas library offers various useful functions and features to make all algorithms and functions faster and easier to design and implement.
"""



# Change some properties if testing code
testing = True
datasize = 100 if testing else len(cities)
figsize = (5, 5) if testing else (10, 10)

# Create data set with specified size
sub = cities.head(datasize)



# Data Structure 2: Array Queue

# Empty class from textbook (ch06)
class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

# ArrayQueue class from textbook (ch06)
class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        """Resize to a new list of capacity >= len(self)."""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

"""
The array queue data structure is used in the calculate_total_distance function to queue distances calculated to then be added summed together to find the total distance a given path takes. The reason this data structure was chosen is because it is practical if the circumstances were changed. For example, if it was required that the path end after a given distance, or after a given number of stops, the queue loop can just end as required, since the distances are added in order of travel.
"""



# Creating common functions

# Create functions to determine distances
def calculate_distance(City1, City2):
    """ Calculate the distance between two cities """
    x = (City2.X - City1.X)**2
    y = (City2.Y - City1.Y)**2
    return (x + y)**0.5

def calculate_total_distance(cities, path):
    """ Calculate total distance from provided path """
    distances = ArrayQueue()
    
    for i, CityId in enumerate(path):
        if i > 0 and i < len(path)-1:
            distance = calculate_distance(cities.iloc[CityId-1], cities.iloc[CityId])
            if cities.is_prime[CityId-1] and i % 10 == 0:
                distance += 0.1*distance
            distances.enqueue(distance)
    
    total_distance = 0
    i = 0
    while not distances.is_empty():
        distance = distances.dequeue()
        if i % 10 == 0 and primes[i-1]:
            total_distance += 0.1*distance
        total_distance += distance
        i += 1
    return total_distance

def display_sample_path(cities):
    """ Creates a graph representing a path to a limited length """
    sample_amount = 50 # Show sample with this many cities from the start of the full DataFrame
    sample = cities.iloc[:sample_amount]

    print(f'The path represented only shows {sample_amount} cities because it gives a clearer representation of how the algorithm works than if every point were to be used. If that were the case, different algorithms would look indistinguishable as {len(sub)} points on a small map would be indistinguishable.')

    plt.figure(figsize=figsize)
    plt.scatter(sample.X, sample.Y, color='#e74c3c', s=10)
    plt.plot(sample.X, sample.Y, color='#e74c3c')
    plt.title(f'Sample path from first {sample_amount} cities in path')

"""
The time complexity for the calculate_distance function is O(1) because it is only running basic arithmetic.

The time complexity for the calculate_total_distance function is O(n) because it has a loop iterating through all n running an O(1) function on each.
"""



# Algorithm 1: Quick Sort

qs = sub.copy()

def quicksort(cities):
    """ Returns path taken by the quicksort algorithm """
    def quicksort_algorithm(cities, low, high):
        """ Modified version of the quicksort algorithm at https://en.wikipedia.org/wiki/Quicksort """
        if low < high:
            p = partition(cities, low, high)
            quicksort_algorithm(cities, low, p-1)
            quicksort_algorithm(cities, p+1, high)
        return cities
    
    def partition(cities, low, high):
        """ Modified version of the partition algorithm at https://en.wikipedia.org/wiki/Quicksort """
        pivot = cities.X[int((high+low)/2)]
        i = low - 1
        j = high + 1
        while True:
            if i % int(len(cities)/10) == 0:
                print(i, j)
            while True:
                i += 1
                if cities.X[i] >= pivot:
                    break
            while True:
                j -= 1
                if cities.X[j] <= pivot:
                    break
            if i >= j:
                return j
            temp = cities.iloc[i]
            cities.at[i] = cities.iloc[j]
            cities.at[j] = temp
    
    #cities = cities.iloc[1:]
    cities = cities.drop(0)
    cities = cities.reset_index(drop=True)
    quicksort_algorithm(cities, 0, len(cities)-1)
    return [0] + list(cities['CityId'])

# Set order from quicksort to sub1
qs_path = quicksort(qs)
qs = qs.reindex(qs_path)
qs = qs.append(qs.iloc[0], ignore_index=True) # Return to North Pole as final point

# Calculate distance using path
qs_distance = calculate_total_distance(qs, qs_path + [len(qs)-1]) # Add final point to path to calculate distance
print(f'Total distance of path: {qs_distance}')

display_sample_path(qs)

"""
The time complexity for the quicksort algorithm is dependent on the current sorting of the cities. In the worst-case scenario, it would take O(n^3) where the data set the algorithm is applied to is already sorted. However, in a best-case scenario, it can take as little as O(n log n) time to complete. It works by halving each slice of the data set (initially the whole set) and sorting the contents of the slice by swapping values of equal distance from top and bottom. It then halves each new slice and repeats the process until each slice only conains a single entry.

This algorithm, while better than a randomised or default path, is still not very optimised, as it is zig zagging vertically because it has been sorted by only the X value of the coordinate of the city. This means two cities can be right next to each other but the algorithm will jump all the way to the bottom of the map to add a city that is horizontally in-between the two.
"""



# Algorithm 2: Greedy Algorithm

gs = sub.copy()

def greedy(cities):
    """ Returns the path taken by the greedy algorithm as described at https://stemlounge.com/animated-algorithms-for-the-traveling-salesman-problem/ """
    cities['visited'] = [False for i in range(len(cities))] # Add visited attribute to DataFrame
    path = []
    head = 0
    while len(path) < len(cities):
        if len(path) % 10000 == 0 and len(path) != 0:
            print(f'Completed {len(path)} cities')
        path.append(head)
        cities.at[head, 'visited'] = True
        for i in [i for i in [0.1, 0.5, 1, 5, 10, 50, 100, 500, 1000, 5000]]: # Gradually increase search range
            possible_cities = cities[
                (cities['X'] - cities.X[head] < i) &
                (cities['Y'] - cities.Y[head] < i) &
                ((cities['visited'] == False))
            ]
            if len(possible_cities) > 0:
                shortest_distance = np.inf # Set value to infinity so any new value is the new shortest
                closest_city = None
                for city in possible_cities.iloc:
                    distance = calculate_distance(cities.iloc[head], city)
                    if (len(path)+1) % 10 == 0 and not cities.is_prime[head]: # Consider extra distance added for non-primes on each 10th
                        distance += 0.1*distance
                    if distance < shortest_distance:
                        shortest_distance = distance
                        closest_city = city
                head = closest_city.CityId
                break
    return path

# Set order from greedy algorithm to sub2
gs_path = greedy(gs)
gs = gs.reindex(gs_path)
gs = gs.append(gs.iloc[0], ignore_index=True) # Return to North Pole as final point

# Calculate distance using path
gs_distance = calculate_total_distance(gs, gs_path + [len(gs)-1]) # Add final point to path to calculate distance
print(f'Total distance of path: {gs_distance}')

display_sample_path(gs)

"""
The time complexity for the greedy algorithm is dependent on the position of the points within the data set. The algorithm works by slowly increasing its theshold for cities to compare its distance to, avoiding it from running O(n log n) as it would if it had to check every remaining city on each iteration using the current data. Once it finds its nearest neighbour, it hops to that and makes it the new head to repeat until all cities have been visited. Theoretically, the worst-case scenario where every cities' position was extremely close together to the point the threshold accepted all points, the time complexity would be O(n log n). In the best-case scenario where every city is only this treshold limit distance between two other cities, resulting in a linked reaction where it only iterates the single new unvisited city, the time complexity would be O(n).

Comparing the overall distance of this algorithm to the basic quick sort, this method is far faster. The worst-case speed of this algorithm is equal to that of the best-case for the quicksort, meaning it is guaranteed it will be faster overall. As well as this, becuase it determines its next city to travel to by its distance from the head, it will also almost certainly return a shorter overall distance, because it doesnt simply sort values by X and zig zagging across the map like quicksort does. It doesn't consider the future effects of a path it takes so it is prone to un-optimised moving, but is still far better than quick sort.
"""



# Submission

path = qs_path + [0] if qs_distance < gs_distance else gs_path + [0]
df = pd.DataFrame({'Path': path})
df.to_csv('Final_Submission.csv', index=False) # Create csv with best path