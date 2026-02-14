x="Hello World"    
print(x)
print(type(x))

x=20.9
print(type(x))

x=range(7)
print(x)
print(type(x))

x=5
y=3.14
z="Hello"
print(type(x))
print(type(y))
print(type(z))
 
#type conversion
x=1 #int
y=2.9 #float
z=1j  #complex
#convert from int to float
a=float(x)
#convert from float to int
b=int(y)
#convert from int to complex
c=complex(x)

print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

#create a list with different data types
mylist = ["Hello", 1, 3.14, True]
print(mylist)

x=7
y=7.8
#convert int to float
a=float(x)
print(a)

dict={"name": "John", "age": 30, "city": "New York"}
print(dict)

#x="python"
#x[0]="j"
#print(x) #strings are immutable, so we cannot change their characters it gives an error

a={1,2,3}
b={3,4,5}
print(a & b) #intersection of sets
print(a | b) #union of sets
print(a - b) #difference of sets

print(5//2)
print(-5//2)#// is floor division(it rounds down to the nearest whole number)

a=3.0
b=3
print(a==b) #true because they have the same value
print(a is b) #false because they are different objects in memory

#largest of three numbers
x,y,z=10,20,15
print(max(x,y,z))

#separate real and imaginary parts of a complex number
c=2+3j
print(c.real) #real part
print(c.imag) #imaginary part

#average of two numbers
a=5
b=10
avg=(a+b)/2 #avg=sum of nos/count of nos
print(avg)

#average using list
numbers=[5,10,15]
avg=sum(numbers)/len(numbers) #avg=sum of nos/count of nos
print(avg)

#creating a complex function using complex
z=complex(2,3) #creates a complex number with real part 2 and imaginary part 3
print(z)

#adding two complex numbers
z1=complex(1,2)
z2=complex(3,4)
z3=z1+z2
print(z3)





