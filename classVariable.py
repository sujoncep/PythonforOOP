class Circle:
    def __init__(self, radious, pi):
        self.radious = radious
        self.pi = pi

    def circumference(self):
        circumference = 2*self.pi*self.radious
        return circumference

    def area(self):
        area = self.pi*self.radious*self.radious
        return area

    def display(self):
        print("The area of the circle is ", self.area())
        print("The circumference of the circle is ", self.circumference())


circle1 = Circle(34, 3.1416)
circle2 = Circle(20, 3.1416)
print(circle1.display())
