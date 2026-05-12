#abstract method
#shape area (basic)
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# object creation
rect = Rectangle(5, 3)
circle = Circle(4)

print("Area of rectangle:", rect.area())
print("Area of circle:", circle.area())


#vechicle system

from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


# Child class Car
class Car(Vehicle):
    def start(self):
        print("Car is starting with a key")


# Child class Bike
class Bike(Vehicle):
    def start(self):
        print("Bike is starting with a kick")


# Testing
car = Car()
bike = Bike()

car.start()
bike.start()