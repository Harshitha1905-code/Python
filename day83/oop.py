#3 to 6 problems
#vechicle rent calculation
# Base class
class Vehicle:
    def display_type(self):
        print("Vehicle")

    def calculate_rent(self, days):
        pass
# Bike class
class Bike(Vehicle):
    def display_type(self):
        print("Bike")

    def calculate_rent(self, days):
        return days * 200
# Car class
class Car(Vehicle):
    def display_type(self):
        print("Car")

    def calculate_rent(self, days):
        return days * 1000
# Bus class
class Bus(Vehicle):
    def display_type(self):
        print("Bus")

    def calculate_rent(self, days):
        return days * 2500
# Objects
b = Bike()
c = Car()
bs = Bus()

b.display_type()
print("Rent:", b.calculate_rent(3))

c.display_type()
print("Rent:", c.calculate_rent(3))

bs.display_type()
print("Rent:", bs.calculate_rent(3))

#payment system using polymorphism
class Payment:
    def process_payment(self, amount):
        pass

# Subclasses for different payment methods
class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

class DebitCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing debit card payment of ${amount}")

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# Objects
credit_card = CreditCardPayment()
debit_card = DebitCardPayment()
paypal = PayPalPayment()

credit_card.process_payment(100)
debit_card.process_payment(200)
paypal.process_payment(300)

#bank account system
# Base class
class Account:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        pass


# Savings Account
class SavingsAccount(Account):
    def add_interest(self):
        interest = self.balance * 0.05
        self.balance += interest
        print("Interest Added:", interest)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")


# Current Account
class CurrentAccount(Account):
    minimum_balance = 1000

    def withdraw(self, amount):
        if self.balance - amount >= self.minimum_balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Minimum balance should be maintained")


# Objects
s = SavingsAccount(5000)
s.deposit(1000)
s.withdraw(2000)
s.add_interest()
print("Savings Balance:", s.balance)

print()

c = CurrentAccount(5000)
c.withdraw(4500)
print("Current Balance:", c.balance)