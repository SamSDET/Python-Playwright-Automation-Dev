class Animal:
    location="Germany"
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("Generic animal sound",self.name)

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Woof!")

a = Animal("Dog")
#a.speak()
d=Dog("Bruno")
d.speak()
a.speak()
print(d.location)

class Hi:
    def firstProgram(self):
        print("Hi World") 
a=Hi()
a.firstProgram()


    


