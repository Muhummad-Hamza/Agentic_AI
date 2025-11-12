# Topic 3: Lists (5 Assignments)

# Assignments no 1
# Student Names
# Task: Make a list of 5 student names. Then, add one new name to the list using .append() and remove one existing name using .remove().

print("\nLists\nAssignment no 1\n")
print("Student Names\n")
student_names = ["Hammad", "Hamza", "Anus", "Sara", "Fatima"]
print("List of Students:", student_names)  
student_names.append("Maria")
print("After appending Maria:", student_names)  
student_names.remove("Sara")
print("After removing Sara:", student_names, "\n")   
print("Final list of students:",student_names)


# Assignments no 2
# Shopping List
# Task: Make a list of 5 grocery items. Replace one item (e.g., change 'milk' to 'butter'). Print the updated list and the total number of items in the list.

print("Lists\nAssignment no 2\n")
print("Shopping List\n")
grocery_items = ["milk", "eggs", "bread", "apples", "bananas"]
print("Original grocery list:", grocery_items)
grocery_items[0] = "butter"
print("Updated grocery list:", grocery_items)
print("Total number of items:", len(grocery_items), "\n")

# Assignments no 3
# Sorting Practice
# Task: Make a list of random numbers. Print the list before and after sorting it using the .sort() method.

print("Lists\nAssignment no 3\n")
print("Sorting Practice\n")
random_numbers = [42, 7, 19, 3, 25, 88, 56]
print("Original list of numbers:", random_numbers)
random_numbers.sort()
print("Sorted list of numbers:", random_numbers, "\n")


# Assignments no 4
#  Favorite Movies
# Task: Store 4 movie names in a list. Print:
# The first two movies
# The last movie
# The total number of movies

print("Lists\nAssignment no 4\n")
print("Favorite Movies\n")
favorite_movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight"]
print("Favorite movies list:", favorite_movies)
print("First two movies:", favorite_movies[:2])
print("Last movie:", favorite_movies[-1])
print("Total number of movies:", len(favorite_movies), "\n")


# Assignments no 5
# Sum of Numbers
# Task: Make a list of numbers [5, 10, 15, 20]. Print:
# The total sum of the numbers using sum()
# The average of the numbers

print("Lists\nAssignment no 5\n")
print("Sum of Numbers\n")
numbers = [5, 10, 15, 20]
total_sum = sum(numbers)
average = total_sum / len(numbers)
print("List of numbers:", numbers)
print("Total sum of numbers:", total_sum)
print("Average of numbers:", average, "\n") 


