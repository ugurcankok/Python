from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Shape = super class / abstract class
    """

    # abstract method
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    # override and polymorphism
    def toString(self):
        pass


class Square(Shape):
    def __init__(self, edge):
        self.__edge = edge  # __ It means that variable will be private, encapsulation.

    def area(self):
        result = self.__edge ** 2
        print("Square area is equal to ", result)

    def perimeter(self):
        result = self.__edge * 4
        print("Square perimeter is equal to ", result)

    def toString(self):
        print("Square edge: ", self.__edge)


class Circle(Shape):
    PI = 3.14  # constant

    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        result = self.PI * self.__radius ** 2
        print("Circle area is equal to ", result)

    def perimeter(self):
        result = 2 * self.PI * self.__radius
        print("Circle perimeter is equal to ", result)

    def toString(self):
        print("Circle radius: ", self.__radius)


c = Circle(5)
c.area()
c.perimeter()
c.toString()
