# Python basic math operations.
# sum = 1 + 9
# print(sum)

# Builtin function operations
from datetime import date                      

# convert date to string.
# print("Today's date is: " + str(date.today()))

# Command-line arugments.
import sys

# print(sys.argv) 
# print(sys.argv[0]) # program name
# print(sys.argv[1]) # first arg 

# Capture user input
# print("welcome to the greeter prgoram")
# name = input("Enter your name: ")
# print("Greetings " + name)

# Working with numbers
print("calculator progrram")
first_number = input("First number: ")
second_number = input("Second number: ")
print("The result of the calculated number is: ", int(first_number) + int(second_number))
