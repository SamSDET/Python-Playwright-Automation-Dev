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

def calculate_area(l,w=10):
    return l * w
l1=float(input("Enter length of rectangle: "))
w1=float(input("Enter width of rectangle (or press Enter to use default 10): ") or 10)
print("Area of rectangle:", calculate_area(l1, w1))

add = lambda x, y: x + y
num1 = float(input("Enter first number to add: "))
num2 = float(input("Enter second number to add: ")) 
print("Sum:", add(num1, num2))

square = lambda x: x * x
list1 =[1,2,3,4,5]
print(list(map(square, list1)))

def factorial(n):
    if n==0 or n==1:
        return 1
    return factorial(n-1)*n
num = int(input("Enter a number to find its factorial: "))
print("Factorial of", num, "is", factorial(num))

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)
    
n = int(input("Enter a number to find the sum of its digits: "))
print("Sum of digits:", sum_of_digits(n))
import math
a= math.sqrt(144)
b = math.sin(math.radians(90))
print(a,b)

import requests
a = requests.get("https://api.github.com")
print(a.status_code)
print(a.json())

def fibonacci(n):
    def fib(k):
        if k <= 1:
            return k
        return fib(k - 1) + fib(k - 2)

    for i in range(n):
        print(fib(i), end=" ")

# Example usage
fibonacci(10)   # Prints: 0 1 1 2 3 5 8 13 21 34
marks = [78, 85, 62, 90, 55]
marks.append(63)
print("Updated marks:", marks)
marks.remove(62)
marks.pop(2)
print("Marks after removal:", marks)
a=5
table =[]
for i in range(1,11):
    table.append(a*i)   
print(table)
table=[6*i for i in range(1,11)]
print(table)
a = (3,2,22,13)
print(a)
set = {1,2,3,4,5}
set.add(21)
set.remove(1)
set.discard(2130)
print(set)
a = {3,23,1}
b = {23,4,2,55,1}
c= a.union(b)
d = a.intersection(b)
print(c,d)
score = {'Harry': 85, 'John': 92, 'Emma': 78}
print(score)
print(score['John'])
#print(score[85])
table_of_5= {i: 5*i for i in range(1,11)}
print(table_of_5)
