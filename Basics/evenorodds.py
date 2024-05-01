
"""_
summary_

Program to read if a number is even or and odd number

"""
    
    
# x = int(input("Enter a number "))

# if x % 2 == 0:
#     print("This is an Even number")
    
# else:
#     print("This is an Odd number")
    
"""_summary_

Using function to give feed back
"""

def main():
    
    x = int(input("what's X "))
    if is_even(x):
        print("Even number")
    else:
        print("Odd number")
        
            
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
            
main()