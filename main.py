# Print
from tty import IFLAG

# In Python, comments start with `#`. The computer ignores everything
# following `#` on the same line. Comments explain the code to human
# readers and do not affect program execution.


print("Hello world")
# The print() function displays the specified content on the screen
# The string "Hello world" is passed as an argument inside the parentheses

print("it's really good")
# This is another call to print()
# Here we print the string "it's really good"


# Variables

# Variable - String

# String variables store text


first_name = "M_Lashkevych"

# Create a variable named first_name and assign it a value
# A variable is like a named container for storing data
# The "=" sign assigns a value to a variable
# "M_Lashkevych" is a string value (text) enclosed in quotes

print(f'Hello {first_name}')

# F-strings make it easy to insert variable values into a string
# Print a greeting using the value of first_name
# print() is a function that displays information on the screen
# f'...' is an f-string that inserts variable values directly into text
# {first_name} in the f-string is replaced with the variable's actual value

food = "pizza"
print (f"You like {food}")
email = "lashkevych2004"
print(f"My email is: {email}")

# Variable - Integers

# An integer is a whole number with no fractional part.
# An integer must not be enclosed in quotes

# Declare integer variables
age = 20  # Create age and assign it the value 20
quantity = 3  # Create quantity and assign it the value 3
num_of_students = 30  # Create num_of_students and assign it the value 30

# Display information using f-strings
print(f"You're {age} years old")  # Print a string containing the value of age
print(f"You're buying {quantity} items")  # Print a string containing the value of quantity
print(f"You class has {num_of_students} students")  # Print a string containing the value of num_of_students

# Variable - float
# Float is a data type for decimal numbers (numbers with a fractional part)

# Declare float variables
price = 10.99  # Create price and assign it the value 10.99
gpa = 3.2      # Create gpa and assign it the value 3.2
distance = 5.5 # Create distance and assign it the value 5.5

# Display information using f-strings
print(f"The price is ${price}")  # Print a string containing the value of price
print(f"Your gpa is: {gpa}")     # Print a string containing the value of gpa
print(f"You run {distance}km")   # Print a string containing the value of distance

# Variable - Boolean
# Boolean is a data type with only two values: True or False.

# Declare Boolean variables
is_student = False   # Create is_student and assign it the value False
for_sale = False     # Create for_sale and assign it the value False
is_online = True     # Create is_online and assign it the value True

# Display information using f-strings
#print(f"Are you a student?: {is_student}")
   # This line would print "Are you a student?: False"

# if condition:
    # code to run if the condition is true
# else:
    # code to run if the condition is false

if is_online:
    print("You're online")
else:
    print("You're offline")
   # This branch runs because is_online is True
   # Prints "You're online"
