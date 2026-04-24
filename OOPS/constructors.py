class Emplyoee:
    company="Asus"
    def __init__(self,salary,name,exp,company):
        self.a=salary
        self.b=name
        self.c=exp
        self.company=company
    def Info(self):
     print(f"The salary of emplyoee is:{self.a}")
     print(f"The Name of Emplyoee is: {self.b}")
     print(f"The experience is:{self.c}")
     print(f"The Company is:{self.company}")
    
e1=Emplyoee(71000,"john Doe", 4,"Apple")
e1.Info()
print(e1.company)
print(Emplyoee.company)



