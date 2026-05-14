#problem on inheritance super() keyword
class Employee:
    def __init__(self, name):
        self.name = name


class Developer(Employee):
    def __init__(self, name, prog_lang):
        super().__init__(name)   # calling parent constructor
        self.prog_lang = prog_lang

    def display(self):
        print("Name:", self.name)
        print("Programming Language:", self.prog_lang)


# object creation
dev = Developer("Nikitha", "Python")
dev.display()

#problem 2 Animal class with multiple child class
class Animal:
    def shout(self):
        print("animal is shouting")


class Dog(Animal):
    def sound(self):
        print("bow")


class Cat(Animal):
    def sound(self):
        print("meow")


# object creation
dog = Dog()
cat = Cat()

dog.shout()
dog.sound()

cat.shout()
cat.sound()
        