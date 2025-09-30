from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def resize(self):
        pass

    @abstractmethod
    def calculateArea(self):
        pass

class Circle(Shape):
    def draw(self):
        print("circle is resizing")

    def resize(self):
        print("Circle is resizing")

    def calculateArea(self):
        r = int(input("Enter radius: "))
        area = 3.14*r*r
        print(f"Area: {area}")

class Rectangle(Shape):
    def draw(self):
        print("rectangle is resizing")

    def resize(self):
        print("rectangle is resizing")

    def calculateArea(self):
        l = int(input("Enter length: "))
        w = int(input("Enter width: "))
        area = l*w
        print(f"Area: {area}")

class Triangle(Shape):
    def draw(self):
        print("triangle is resizing")

    def resize(self):
        print("triangle is resizing")

    def calculateArea(self):
        l = int(input("Enter length: "))
        h = int(input("Enter height: "))
        area = (l*h)/2
        print(f"Area: {area}")

C1 = Circle()
R1 = Rectangle()
T1 = Triangle()

C1.draw()
C1.resize()
C1.calculateArea()

R1.draw()
R1.resize()
R1.calculateArea()

T1.draw()
T1.resize()
T1.calculateArea()