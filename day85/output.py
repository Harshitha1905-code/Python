class Test:

    def __init__(self):
        print("Constructor called")
t = Test()

class A:
    
    def show(self):
        print("Class A")

class B(A):
    pass

b = B()
b.show()



class Animal:
    
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    
    def sound(self):
        print("Dog bark")
d=Dog()
d.sound()


#create class ATMmethods:deposit(),withdraw(),check_balance() use encapsulation
class ATM:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def check_balance(self):
        print("Balance:", self.__balance)
atm = ATM()
atm.deposit(1000)
atm.withdraw(500)
atm.check_balance()

#create parent class as employee method:work() child class:Devoloper Manager 
class Employee:
    def work(self):
        print("Employee is working")
class Developer(Employee):
    def work(self):
        print("Developer is coding")
class Manager(Employee):
    def work(self):
        print("Manager is managing")
e1 = Employee()
d1 = Developer()
m1 = Manager()
e1.work()
d1.work()
m1.work()


#Create Abstract Class:Shape Method:area() Create child classes:Circle Rectangle
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
c = Circle(5)
r = Rectangle(4, 6) 
print("Area of Circle:", c.area())
print("Area of Rectangle:", r.area())


