# Base class
class Animal:
    def sound(self):
        pass
# Subclass Dog
class Dog(Animal):
    def sound(self):
        return "Bark"
# Subclass Cat
class Cat(Animal):
    def sound(self):
        return "Meow"
# Objects
d = Dog()
c = Cat()

print("Dog sound:", d.sound())
print("Cat sound:", c.sound())

#create base class employee sub classses:manager,devoloper,intern and each employee has Manager gets bonus salary,Devoloper gets project allowance,Intern gets stipend,
# Base class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary
# Manager class
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.bonus
# Developer class
class Developer(Employee):
    def __init__(self, name, salary, allowance):
        super().__init__(name, salary)
        self.allowance = allowance

    def calculate_salary(self):
        return self.salary + self.allowance
# Intern class
class Intern(Employee):
    def __init__(self, name, stipend):
        super().__init__(name, 0)
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend
# Objects
m = Manager("Rahul", 50000, 10000)
d = Developer("Anu", 40000, 5000)
i = Intern("Kiran", 8000)

print("Manager Salary:", m.calculate_salary())
print("Developer Salary:", d.calculate_salary())
print("Intern Salary:", i.calculate_salary())

#create abstract class shape and sub classes circle,rectangle and triangle and each shape has area method to calculate area of the shape
from abc import ABC, abstractmethod
# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
# Rectangle class
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
# Triangle class
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
# Objects
c = Circle(5)
r = Rectangle(4, 6)
t = Triangle(4, 5)
print("Circle Area:", c.area())
print("Rectangle Area:", r.area())
print("Triangle Area:", t.area())
    