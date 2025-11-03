square = lambda x: x * x
sum = lambda a, b: a + b
print(square(5))  # Output: 25
print(sum(3, 4))  # Output: 7
 
def fib(n):
    if (n==0 or n==1):
        return n
    else:
     return fib (n-2) + fib(n-1)
    
n=int(input("Enter a number: "))
f=fib(n)
print(f)

f1=0
f2=1
n=int(input("Enter number of terms: "))
print(f1,f2, end=' ')
for i in range(3,n+1):
    f3=f1+f2
    print(f3, end=' ')
    f1=f2
    f2=f3