#create a parent class animal having sound as a method,child class dog having sound as a method
# Parent class
class Animal:
    def sound(self):
        print("Animals make sounds")


# Child class
class Dog(Animal):
    def sound(self):
        print("Dog barks")


# Object creation
a = Animal()
d = Dog()

# Calling methods
a.sound()
d.sound()

#parent class-employe,child class-devoloper,child class-manager
# Parent class
class Employee:
    def show(self):
        print("This is Employee class")


# Child class 1
class Developer(Employee):
    def work(self):
        print("Developer writes code")


# Child class 2
class Manager(Employee):
    def manage(self):
        print("Manager handles team")


# Object creation
d = Developer()
m = Manager()

# Calling methods
d.show()
d.work()

m.show()
m.manage()