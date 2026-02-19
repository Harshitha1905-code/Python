x="Hello,World!"
print(len(x))

#Access first and last character of a string
x="Hello,World!"
print(x[0])
print(x[-1])

#to reverse a string
s = "python"
print(s[::-1])

#to check if a string is palindrome
x="madam"
if x==x[::-1]:
 print("Palindrome")
else:
 print("not palindrome")

 s = "racecar"
 if s == s[::-1]:
    print("Palindrome")
 else:
    print("Not Palindrome")

g="Hello, World!" 
print(g.upper())
print(g.lower())
print(g.title())
print(g.replace("H", "J"))  
print(g.strip()) 

#how many times a character appears in a string
a ="banana"
print(a.count("a"))

#a program to replace all spaces with underscores
a = "Hello World"
b = a.replace(" ", "_")

#checks if a string contains only digits
a = "12345"
print(a.isdigit())


