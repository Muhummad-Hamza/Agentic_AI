# Topic 5: Dictionaries (5 Assignments)

# Assignments no 1
# Create a dictionary named student with the following information:
# student = {
#   "name": "Ali",
#   "age": 20,
#   "grade": "A"
# }

print("\nDictionaries\nAssignment no 1\n")
print("Create Student Dictionary\n")
student = {
    "name": "Ali",
    "age": 20,
    "grade": "A"
}
print("Student Dictionary:", student, "\n")


# Assignments no 2
# Update Dictionary
# Task: Start with the following dictionary:
# car = {"brand": "Toyota", "year": 2020}
# Add a new key color with a value (e.g., "Red"). Update the year to 2022. Print the updated dictionary.

print("Dictionaries\nAssignment no 2\n")
print("Update Car Dictionary\n")
car = {"brand": "Toyota", "year": 2020}
print("Original Car Dictionary after adding color and update year:", car)
car["color"] = "Red"
car["year"] = 2022
print("Updated Car Dictionary:", car, "\n")


# Assignments no 3
# Loop Through Dictionary
# Task: Create a dictionary of 3 countries with their capitals (e.g., Pakistan: Islamabad, Turkey: Ankara, Japan: Tokyo). Loop through the dictionary and print each country and its capital in the format: Country → Capital.

print("Dictionaries\nAssignment no 3\n")
print("Countries and Capitals\n")
countries_capitals = {
    "Pakistan": "Islamabad",
    "Turkey": "Ankara",
    "Japan": "Tokyo"
}   
for country, capital in countries_capitals.items():
    print(f"{country} → {capital}")
print()     


# Assignments no 4
# Dictionary of Prices
# Task: Create a dictionary of 3 products and their prices (e.g., {"apple": 1.5, "banana": 0.75, "orange": 1.2}). Ask the user which product's price they want to see and display it.

print("Dictionaries\nAssignment no 4\n")
print("Product Prices\n")
product_prices = {
    "apple": 1.5,
    "banana": 0.75,
    "orange": 1.2
}   
product = input("Enter the product name (apple, banana, orange): ").strip().lower()
if product in product_prices:
    print(f"The price of {product} is ${product_prices[product]}\n")
else:   
    print(f"Sorry, {product} is not available in the product list.\n")


# Assignments no 5
# Nested Dictionary
# Task: Create a dictionary named students with nested dictionaries for each student's information:
# students = {
#   "Ali": {"age": 18, "grade": "A"},
#   "Sara": {"age": 19, "grade": "B"}
# }
# Loop through the students dictionary and print each student's name along with their grade.

print("Dictionaries\nAssignment no 5\n")
print("Nested Student Dictionary\n")
students = {
    "Ali": {"age": 18, "grade": "A"},
    "Sara": {"age": 19, "grade": "B"}
}
for student_name, info in students.items():
    print(f"{student_name} has grade: {info['grade']}")
print()

