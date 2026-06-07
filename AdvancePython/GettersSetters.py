class Emplyoee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @property    
    def first_name(self):
        l = self.name.split(" ")
        print(l)
        return l[0]
    @first_name.setter
    def first_name(self, first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name

e = Emplyoee("John Down", 30)
#e.projects=6
#print(e.projects)
#print(e.first_name())
#e.set_first_name("Jack")
#print(e.name)

print(e.first_name)
e.first_name ="Jack"
print(e.name)




