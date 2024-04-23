class Circle:
    pi = 3.1416

    def __init__(self, radious):
        self.radious = radious

    def circumference(self):
        circumference = 2*Circle.pi*self.radious
        return circumference

    def area(self):
        area = Circle.pi*self.radious*self.radious
        return area

    def display(self):
        print("The area of the circle is ", self.area())
        print("The circumference of the circle is ", self.circumference())


circle1 = Circle(34)
circle2 = Circle(20)
print(circle1.display())
