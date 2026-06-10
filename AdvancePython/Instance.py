class Employee:
    company="Accenture"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def print_info(self):
        print(f"The Employee Name: {self.name}, and Salary: {self.salary}")
    @staticmethod
    def sum(a,b):
        print(a+b)
    @classmethod
    def print_company(cls):
        cls.company="Experian"
        print(f"The company name is: {cls.company}") 
       

e1 = Employee("John", 95000)
e2 = Employee("Jane", 85000)
print(Employee.company)
e1.print_info()
e2.print_info()
e2.sum(2,3)
Employee.print_company()
print(Employee.company)
