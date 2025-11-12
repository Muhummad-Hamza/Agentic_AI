# Topic 4: Sets (5 Assignments)

# Assignments no 1
# Unique Numbers
# Task: Create a set with some duplicate numbers (e.g., {1, 2, 2, 3, 4, 4, 5}). Print the set to show how duplicates are automatically removed.

print("\nSets\nAssignment no 1\n")
print("Unique Numbers\n")
numbers = {1, 2, 2, 3, 4, 4, 5}
print("Set of unique numbers:", numbers, "\n")


# Assignments no 2
# Set Operations
# Task: Create two sets: A = {1, 2, 3, 4} B = {3, 4, 5, 6}
# Print their:
# Union (all unique elements from both sets)
# Intersection (elements common to both sets)
# Difference (elements in A but not in B)

print("Sets\nAssignment no 2\n")
print("Set Operations\n")
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Set A:", A)
print("Set B:", B)
print("Union of A and B:", A.union(B))
print("Intersection of A and B:", A.intersection(B))
print("Difference of A and B (A - B):", A.difference(B), "\n")


# Assignments no 3
# Adding & Removing
# Task: Create a set {2, 4, 6}. Add the number 8 to the set, then remove the number 4. Print the updated set.

print("Sets\nAssignment no 3\n")
print("Adding & Removing\n")
my_set = {2, 4, 6}
print("Original set:", my_set)
my_set.add(8)
print("After adding 8:", my_set)
my_set.remove(4)
print("After removing 4:", my_set, "\n")    
print("Final set:",my_set)


# Assignments no 4
# Membership Check
# Task: Check if a specific number (e.g., 5) exists in the set {1, 2, 3, 4, 5} using the in keyword. Print True or False.

print("Sets\nAssignment no 4\n")
print("Membership Check\n")
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)
number_to_check = 5
is_member = number_to_check in my_set
print(f"Is {number_to_check} in the set? {is_member}\n")


# assignments no 5
# Convert List to Set
# Task: Given a list [1, 2, 2, 3, 4, 4, 5]. Convert this list to a set to automatically remove duplicates. Print both the original list and the resulting set.

print("Sets\nAssignment no 5\n")
print("Convert List to Set\n")
my_list = [1, 2, 2, 3, 4, 4, 5]
print("Original list:", my_list)
my_set = set(my_list)
print("Set after removing duplicates:", my_set, "\n")    
print("Final set:",my_set)


