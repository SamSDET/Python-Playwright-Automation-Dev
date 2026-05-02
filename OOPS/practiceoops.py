class Car:
    def drive(self):
        print("Car is driving")
p= Car()
p.drive()

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
person1 = Person("Alice", 30)
person1.display()

class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")

D1= Dog()
D1.sound()
