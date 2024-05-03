"""
    int, in python means integer
    
    
    There are symbols supported by python, like
    1. *
    2. +
    3. -
    4. /
    5. % Modulos
"""
    
# Developing a siple calculator

# Concatenating of strings when the user input of the type is string
    
# x = float(input("X value? "))
# y = float(input("Y value? "))

# x = int(input("X value? "))
# y = int(input("Y value? "))

#performing float operation in Python
x1 = float(input("X value? "))
y1 = float(input("Y value? "))

# x = int(x)
# y = int(y)


# PYTHON ROUNDING;
# round(number[, ndigits])
z = round(x1 / y1, 2) # Only the round alone will return on digits here
print("Result summation is ", end='')

# Using FString too to format a number..

# Fstring approach to runding numbers
print(f"{z:,}")

print(f"F-string approach {z:.2f}", )

# I can also use; 
# x = int(input("What's x " ))
# y = int(input("What's y "))

