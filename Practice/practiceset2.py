'''i=int(input("Enter a number to identify: "))
if(i>0):
 print("The number is positive")
elif(i<0):
 print("The number is negative")
else:
 print("The number is zero")

age = int(input("Enter your age: "))
if(age>=18):
 print("You are eligible to vote")
else:
 print("You are not eligible to vote")

 eo=int(input("Enter the number to check if it is a even or odd: "))
 if(eo%2==0):
    print("The number is even")
 else:
    print("The number is odd") 

daynum = int(input("Enter the day number (1-7): "))
match daynum:
   case 1: 
      print("Monday")
   case 2:
      print("Tuesday")    
   case 3:   
      print("Wednesday")
   case 4:     
      print("Thursday")
   case 5:     
      print("Friday")   
   case 6:     
      print("Saturday")
   case 7:     
      print("Sunday")
   case __:
      print("Invalid day number")

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
opeartor=input("Enter the operator (+, -, *, /): ")
match opeartor:
      case '+':
         print("The sum is:"+str(num1 + num2))
      case '-':
         print(f"The difference is: {num1 - num2}")
      case '*':
         print(f"The product is: {num1 * num2}")
      case '/':
         if num2 != 0:
               print(f"The quotient is: {num1 / num2}")
         else:
               print("Error: Division by zero")
      case _:
         print("Invalid operator")

for i in range(1,11):
    print(i,end=' ')

multp= int(input("\nEnter the number to print its multiplication table: "))
for i in range(1,11):
    print(f"{multp} x {i} = {multp*i}")


sum=0
for i in range(1,101):
    sum=sum+i
print(f"The sum of first 100 natural numbers is: {sum}")
for i in range(1,5):
    print("*"*i)

sum=0;i=1 
while i<=100:
    sum +=i
    i+=1
print(f"The sum of first 100 natural numbers is: {sum}") 

password="1@"
enter_password=input("Enter the password: ")
while enter_password!=password:
    print("Incorrect password, try again.")
    enter_password=input("Enter the password: ")
print("Access granted.")

num=int(input("Enter a number to reverse: "))
print(int(str(num)[::-1]))

for i in range(1,11):
    if i==7:
         break
    print(i,end=' ') '''


           



