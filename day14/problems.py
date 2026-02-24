#operators problems
a=10
b=5
print(a+b) #addition
print(a-b) #subtraction
print(a*b) #multiplication
print(a/b) #division

a=10
b=5
#find the remainder of a divided by b
print(a%b) #modulus

a = 3
print(a**2) #square of a number
print(a**3)#cube of a number

#assignment operators
x=10
x+=5 #x=x+5
print(x)
x-=3
print(x)
x*=2
print(x)

#variables value changes step by step
x=10
print(x)
x+=5
print(x)
x-=3
print(x)

#comaprison operators
#Take two numbers as input and check:if they are equal,which one is greater
a = 10
b = 20
if a == b:
    print("a and b are equal")
else:
    print("a and b are not equal")
if a > b:
        print("a is greater than b")
else:
        print("b is greater than a")  


#check whether a number is positive,negative or zero
x = 6
if x > 0:
    print("x is positive")
if x < 0:   
      print("x is negative")
if x == 0:  
      print("x is zero")  

#check if a person is eligible to vote or not        
age = 17
if age >= 18:
    print("You are eligible to vote")
else:
      print("You are not eligible to vote") 

#logical operators
# check if a number lies between 10 and 50
x = 5
if x > 10 and x < 50:
    print("x lies between 10 and 50")
else:
    print("x does not lie between 10 and 50")

#take a username and password and check:access granted if both are correct,access denied otherwise
username = "admin"
password = "password123"
if username == "admin" and password == "password123":
    print("Access granted")
else:
    print("Access denied")   

  #using not 
a = 10
print(not a > 20)  

#bitwise operators
print(6 & 3) #bitwise AND
print(6 | 3) #bitwise OR
print(6 ^ 3) #bitwise XOR

#WAP to left shift and right shift a number by 1
x = 4 #in binary 100
print(x << 1) #left shift by 1, result is 8 (in binary 1000)
print(x >> 1) #right shift by 1, result is 2 (in binary 10)

#check even or odd using operators
x = 5
if x % 2 == 0:
    print("x is even")
else:    print("x is odd")

#check whether a number is divisible by 3 and 5
x = 15
if x % 3 == 0 and x % 5 == 0:
    print("x is divisible by 3 and 5")
else:    print("x is not divisible by 3 and 5")    
