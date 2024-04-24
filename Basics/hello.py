print("Hello world!")

# "PRINT" is a function
# "AGUEMENT" is the string of text that the print fuction accepts
# The thing that appear in the screen after runninng the  code is called "SIDE EFFECT"


# Accepting input

# input("What is your name ", )
# print("Hello Michael!")

# Getting users input and hand it back
# Using return value;;;;  1. Variables

# name = input("What is your name ")

# print("Hello ", name)

# Looking deeper into print function

# name = input("Please repeat that your name ")

# print("Hello ", end="" sep="HEL")

# end and sep are called named positional parameters

# Using quotes inside quotes, This can be achieved by using single quote outside and 
# using double quotes inside of the strings
#
# print('Hello "Michael" ')

# 2. By using Escape characters 
# print("Hello Michael \"Come Here\" ")

# 3 Using FString
# applying some methods
# name = input("Enter your name ").strip().title()  # shorter version of the code
# name = name.strip()
# name = name.title()

# Splittting users name into firstname and last name

name = input("I want to split, What is your name? ")
name = name.split(' ')
print(f"Hello {name[0]}")