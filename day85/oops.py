# Create a class Student with:
#attributes: name, marks
#method: display()
#Create 3 student objects and print their details.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)
student1 = Student("Alice", 85)
student2 = Student("Bob", 90)
student3 = Student("Charlie", 78)
student1.display()
student2.display()
student3.display()

#Create a class Rectangle with:length,breadth Methods:area(),perimeter()
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)
rect = Rectangle(5, 3)

print("Area:", rect.area())
print("Perimeter:", rect.perimeter())

#create a class Circle with: radius Methods: area(), circumference()
class circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    def circumference(self):
        return 2 * 3.14 * self.radius
c = circle(4)
print("Area:", c.area())
print("Circumference:", c.circumference())

#create a class mobile with:brand,price,color,create multiple objects and print all details.
class Mobile:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def display(self):
        print("Brand:", self.brand)
        print("Price:", self.price)
        print("Color:", self.color)
mobile1 = Mobile("Apple", 999, "Black")
mobile2 = Mobile("Samsung", 799, "White")
mobile3 = Mobile("OnePlus", 699, "Red")
mobile1.display()   
mobile2.display()
mobile3.display()

#constructor init problems
#create an employee class using constructor to initialize:id,name,salary.Add a method to display details.
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)

emp1 = Employee(101, "John Doe", 50000)
emp2 = Employee(102, "Jane Smith", 60000)
emp1.display()
emp2.display()

#create a class bankaccount:deposit(),withdraw(),checkbalance() using constructor to initialize account holder name and balance.
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Balance:", self.balance)


b = BankAccount("Harsha", 1000)

b.deposit(500)
b.withdraw(300)
b.check_balance()

#create a car class with instructor:attributes:company,model,year.add method car_info.
class Car:
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year = year

    def car_info(self):
        print("Company:", self.company)
        print("Model:", self.model)
        print("Year:", self.year)
car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)
car1.car_info()
car2.car_info()


