#parent-payment, child-upi, child-card---method=pay(self, amnt)
# Parent class
class Payment:
    def pay(self, amount):
        print(amount)


# Child class
class UPI(Payment):
    def pay(self, amount):
        print("UPI Payment:", amount)


# Child class
class Card(Payment):
    def pay(self, amount):
        print("Card Payment:", amount)


# Objects
u = UPI()
c = Card()

u.pay(500)
c.pay(1000)