#encapsulation problems
#create a class ATM:balance should be private,methods:deposit(),withdraw(),check_balance(),do not allow direct access to balance
class ATM:
    def __init__(self):
        self.__balance = 0   # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited:", amount)
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Balance:", self.__balance)

#inheritance problems
# create a parent class vechicle methods:start() create child classes:car,bike.both should inherit start()
class Vehicle:
    def start(self):
        print("Vehicle started")
class Car(Vehicle):
        def start(self):
            print("Car started")
    
class Bike(Vehicle):
        def start(self):
            print("Bike started")
v = Vehicle()
v.start()
c = Car()
c.start()
b = Bike()
b.start() 

#animal class:method:sound() create child classes:dog,cat, cow.Each should override sound() method.
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
class Cow(Animal):
    def sound(self):
        print("Cow moos")
a = Animal()
a.sound()
d = Dog()
d.sound()
c = Cat()
c.sound()
w = Cow()
w.sound()

#polymorphism problems
#create parent class shape:child classes:circle,square.override method area()
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
c = Circle(5)
print("Area of Circle:", c.area())
s = Square(4)
print("Area of Square:", s.area())

#abstraction problems
#create an abstract class:vechicle abstract methods:start(),stop(),child classes:car,bike
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")
class Bike(Vehicle):
    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike stopped")
c = Car()
c.start()   
c.stop()
b = Bike()
b.start()
b.stop()

#shape abstract class:abstract method_area()child classes:rectangle,trianlge,circle
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
r = Rectangle(5, 3)
print("Area of Rectangle:", r.area())       
t = Triangle(4, 6)
print("Area of Triangle:", t.area())
c = Circle(5)
print("Area of Circle:", c.area())

#multiple inheritance problems
#create father,mother,child classes:child should inherit properties of both father and mother
class Father:
    def __init__(self, name):
        self.name = name

    def display_father(self):
        print("Father's Name:", self.name)
class Mother:
    def __init__(self, name):
        self.name = name

    def display_mother(self):
        print("Mother's Name:", self.name)
class Child(Father, Mother):
    def __init__(self, father_name, mother_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)

    def display_child(self):
        print("Child's Father:", self.name)
        print("Child's Mother:", self.name)
child = Child("John", "Jane")
child.display_father()
child.display_mother()
