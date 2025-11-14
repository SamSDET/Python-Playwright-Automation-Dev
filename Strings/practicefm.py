import math
def square(a):
    return a*a
q=int(input("Enter a number to find its square : "))
print(square(q))

def full_name(first, last):
    return first + " " + last
f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
print("Full Name:", full_name(f_name, l_name))
