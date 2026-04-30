class Vector:
    def __init__(self,a,b):
        self.x = a
        self.y = b
    def sum(self,p):
        return Vector(self.x + p.x, self.y + p.y)
    def __add__(self, p):
        return Vector(self.x + p.x, self.y + p.y)
    def print_point(self):
        print(f"({self.x},{self.y})")

p1 = Vector(3,2)
p2 = Vector(6,5)
p =p1.sum(p2)
print(p.x)
print(p.y)
p.print_point()
#p= p1 + p2



