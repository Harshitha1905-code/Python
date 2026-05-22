# 3. Employee Salary Management

class Employee:
    def __init__(self):
        self.__salary = 0   # private variable

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative")

    def get_salary(self):
        return self.__salary


# Example
e = Employee()

e.set_salary(50000)

print(e.get_salary())

# 4. Mobile Phone Lock System

class Mobile:
    def __init__(self):
        self.__password = ""   # private variable

    def set_password(self, password):
        self.__password = password

    def check_password(self, password):
        if password == self.__password:
            return "Phone Unlocked"
        else:
            return "Wrong Password"


# Example
m = Mobile()

m.set_password("1234")

print(m.check_password("1234"))
print(m.check_password("5678"))