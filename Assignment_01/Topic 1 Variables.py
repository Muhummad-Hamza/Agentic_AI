# Topic 1: VARIABLES (5 Assignments)

# Assignments no 1
# Simple Calculator
# Objective: Practice numeric variables and arithmetic. Task: Create two variables num1 and num2 and print their sum, difference, product, and division.

print("\nVariables\nAssignment no 1\n")
print("Simple Calculator\n")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number:"))

print("\nSum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Division:", num1 / num2,"\n") 

# Assignments no 2
#  Personal Info Card
# Objective: Combine string and numeric variables. Task: Store your name, age, and favorite hobby in variables and print:

print("Variables\nAssignment no 2\n")
print("Personal Info Card\n")

name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobby = input("Enter your favorite hobby: ")

print(f"\nHi, I'm {name}. I'm {age} years old and I love {hobby}.\n")

# Assignments no 3
# Temperature Converter
# Objective: Use expressions. Task: Convert Celsius to Fahrenheit using the formula: (celsius * 9/5) + 32.

print("Variables\nAssignment no 3\n")
print("Temperature Converter\n")

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"\nFahrenheit: {fahrenheit}°F\n")

# Assignments no 4
# Area of Rectangle
# Objective: Logical math with variables. Task: Calculate the area of a rectangle using the formula: length * width.

print("Variables\nAssignment no 4\n")
print("Area of Rectangle\n")

length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
area = length * width

print(f"\nArea of Rectangle: {area}\n")


# Assignments no 5
# Salary Increment
# Objective: Practice updating variable values. Task: Store a salary in a variable and then increase it by 10%. Print both the old and new salary.

print("Variables\nAssignment no 5\n")
print("Salary Increment\n")

salary = float(input("Enter your current salary: "))
new_salary = salary + (salary * 0.10)

print(f"\nOld Salary: {salary}\nNew Salary: {new_salary}\n")

