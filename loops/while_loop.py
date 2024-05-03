# i = 3

# while i != 0:
#     print("meow")
    
#     i = i-1


""" Trying another way """

# i = 0

# while i < 3:
#     print("meow")
#     # i = i + 1
#     i += 1


""" infinite look """

# while True:
#     n = int(input("What's n "))
#     if n < 0:
#         continue
#     else:
#         break
    

# for i in range(n):
#     print("meow")

def main():
    
    number = get_number()
    meow(number)
    
def get_number():
    while True:
        n = int(input("What's n "))
        if n > 0:
            return n


def meow(n):
    for i in range(n):
        print(f'{i} => meow')
        
main()