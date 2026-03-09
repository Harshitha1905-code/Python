#Write a program to store your name, age, and branch in variables and print them in one line.
name="Harshitha"
age=20
branch="CSE"
print(name,age,branch)

#Create variables for integer, float, string, and boolean and print their data types using type().
a=10
b=1.8
c=True
print(type(a))
print(type(b))
print(type(c))

#Write a program that takes two numbers from the user and prints their sum, difference, product, and division.
a=5
b=8
print("Sum:",a+b)
print("Difference:",a-b)
print("Product:",a*b)
print("Division:",a/b)

 #Write a program to swap two numbers using a third variable.
a=5
b=8
temp=a
a=b
b=temp
print("After swapping: a =",a,"b =",b)

#Write a program to swap two numbers without using a third variable.
a=5
b=8
a=a+b
b=a-b
a=a-b
print("After swapping: a =",a,"b =",b)

#Write a program to count the number of characters in a string.
string="Hello, World!"
print(len(string))

#Write a program to convert a string into uppercase and lowercase.
string="Hello, World!"
print(string.upper())
print(string.lower())
