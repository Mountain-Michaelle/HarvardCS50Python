"""

Match is a conditional statement used
in other languages like switch functions

in Python it is called match function  

"""

# For example

name = input("What is your name ")


# if name == "Harryr" or name == "Henry" or name == "Chinedu":
#     print("You are a realtor")
    
# elif name == "Mike":
#     print("Mike is a programmer")
    
# elif name == "Jane":
#     print("Jane is a Tailor")

# else:
#     print("Name not recognized")

""" This code can better be written as """

match name:
    case "Mike" | "michael" | "chinemelu":
        print("You are a programmer")
    case "Uche":
        print("You are a Pianist")
    case "Amara":
        print("You are a nurse")

print(name.upper())