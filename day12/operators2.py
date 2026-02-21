#logical operators
#test if a number is greater than zero and less than 10
x=8
print(x>0 and x<10)

#test if a number is less than 5 or greater than 10
x=5
print(x<5 or x>10)

#reverse the result with not
x=5
print(not(x>3 and x<10))

#is operator returns true if both variables are the same object
x = ["apple", "banana", "cherry"]
y = ["apple", "banana", "cherry"]
z=x
print(x is z)
print(x is y)
print(x == y)

#is not operator returns true if both variables are not the same object
x = ["apple", "banana", "cherry"]
y = ["apple", "banana", "cherry"]
z = x
print(x is not z)
print(x is not y)

x=[1,2,3]
y=[1,2,3]
print(x is y) #is operator checks if both variables point to the same object, not if they have the same content
print(x == y) #checks if values of both variables are equal

#in operator

x = ["apple", "banana", "cherry"]
print("banana" in x)

#not in operator
x=[1,2,3]
print(4 not in x)

fruits=["apple,banana, cherry"]
print("banana" in fruits)

#membership operators can also work with strings
txt = "Hello world"
print("world" in txt)
print("banana" in txt)
print("z" not in txt)

