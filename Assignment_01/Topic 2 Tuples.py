# Topic 2: Tuples (5 Assignments)

# Assignments no 1
# Favorite Fruits
# Task: Create a tuple of 5 fruits and print:
# The first fruit
# The last fruit
# The total number of fruits

print("\nTuples\nAssignment no 1\n")
print("Favorite Fruits\n")

fruits = ("apple", "banana", "cherry", "date", "elderberry")

print("Fruits tuple:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Total number of fruits:", len(fruits), "\n")


# Assignments no 2
# Tuple of Marks
# Task: Make a tuple marks = (78, 82, 90, 67, 88). Print the highest and lowest marks using the max() and min() functions.

print("Tuples\nAssignment no 2\n")
print("Tuple of Marks\n")

marks = (78, 82, 90, 67, 88)

print("Marks tuple:", marks)
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks), "\n")


# Assignments no 3
# Task: Create a tuple of 10 numbers and print:
# The first 3 numbers
# The last 3 numbers
# The middle 4 numbers

print("Tuples\nAssignment no 3\n")
print("Tuple of Numbers\n")

numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

print("Numbers tuple:", numbers)
print("First 3 numbers:", numbers[:3])
print("Last 3 numbers:", numbers[-3:])
print("Middle 4 numbers:", numbers[3:7], "\n")


# Assignments no 4
# Tuple Indexing
# Task: Create a tuple of city names and print:
# The city at index 2
# The city at index -1 (which is the last city)

print("Tuples\nAssignment no 4\n")
print("Tuple Indexing\n")

cities = ("Karachi", "lahore", "Chicago", "Houston", "Phoenix")

print("Cities tuple:", cities)
print("City at index 2:", cities[2])
print("City at index -1:", cities[-1], "\n")


# Assignments no 5
# Count & Find in Tuple
# Task: Create a tuple with repeating colors: ('red', 'blue', 'red', 'green', 'red'). Print how many times "red" appears in the tuple and find its first index.

print("Tuples\nAssignment no 5\n")
print("Count & Find in Tuple\n")

colors = ('red', 'blue', 'red', 'green', 'red')

print("Colors tuple:", colors)
print("Count of 'red':", colors.count('red'))
print("First index of 'red':", colors.index('red'), "\n")



