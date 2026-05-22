# 1. Student Marks System

class Student:
    def __init__(self):
        self.__marks = 0   # private variable

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Marks should be between 0 and 100")

    def get_marks(self):
        return self.__marks


# Example
s = Student()

s.set_marks(85)

print(s.get_marks())

# 2. Bank Account

class BankAccount:
    def __init__(self):
        self.__balance = 0   # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance


# Example
b = BankAccount()

b.deposit(5000)
b.withdraw(2000)

print(b.get_balance())