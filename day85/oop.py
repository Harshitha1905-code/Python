class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
s1 = student("Alice", 85)
s2 = student("Bob", 90)
s1.display()
s2.display()

class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print("Name:", self.name)
        print("Salary:", self.salary)
e1 = employee("John", 50000)
e2 = employee("Jane", 60000)
e1.show_details()
e2.show_details()

#create class bank private variable:balane methods:deposit(),withdraw(),show_balance()
class Bank:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.__balance)
b1 = Bank()
b1.deposit(1000)    
b1.withdraw(500)
b1.show_balance()

#create a vehicle parent class and method start() and create child class car method:drive()
class Vehicle:
    def start(self):
        print("Vehicle started")
class Car(Vehicle):
    def drive(self):
        print("Car is driving")
c1 = Car()
c1.start()
c1.drive()

#polymorphism example
#create class animal method: sound() and create child class dog and cat method: sound()
class Animal:
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Woof")
class Cat(Animal):
    def sound(self):
        print("Meow")

d1 = Dog()
c1 = Cat()
d1.sound()
c1.sound()

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


