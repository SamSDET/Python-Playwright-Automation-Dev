def samad(func):
    def wrapper():
        print("I am about to print Hi")
        func()
        print("I have printed Hi")
    return wrapper
@samad
def SayHi():
    print("Hi")

#SayHi()
#f = samad(SayHi)
#f()
SayHi()

def repeat(n):
    def decorator(func):
        def wrapper(b):
            for i in range(n):
                func(b)
        return wrapper
    return decorator

@repeat(7)
def Say_Hi(a):
    print(f"Hi {a}")

Say_Hi("Samad")



