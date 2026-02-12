myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)


x, y, z = "Orange", "Banana", "Cherry"#python variables can store multiple values in one line
print(x)
print(y)
print(z)


x = y = z = "Orange" #can assign the same value to multiple variables in one line
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python" #output multiple variables separated by comma
y = "is"
z = "awesome"
print(x, y, z)

x = 5 #string and number gets the output when we keep comma
y = "John"
print(x, y)

x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()


def myfunc():  #To create a global variable inside a function, you can use the global keyword.
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)
