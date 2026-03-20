m=("apple","banana","cherry")
print(type(m))

thistuple=tuple(("apple","banana","cherry"))
print(thistuple)

t=("apple","banana","cherry")
print(t[-2])#prints the last second word

t=("apple","banana","cherry")
print(t[:2])#By leaving out the start value, the range will start at the first item:
print(t[1:])#By leaving out the end value, the range will go on to the end of the tuple:

t=("apple","banana","cherry","kiwi","melon")
print(t[-4:-1])

t=("apple","banana","cherry")
if "melon"  in t:
    print("Yes,'melon' is in the t")
else:
    print("No,'melon' is not in t")   

#convert the tuple to list
x=("apple","banana","orange")
y=list(x)
y[1]="kiwi"
x=tuple(y) 
print(x)    

x=("apple","banana","cherry")
y=list(x)
y.append("orange")
x=tuple(y)
print(x)

t=("apple","banana","cherry")
y=("orange",)
t+=y
print(t)

x=("apple","banana","cherry")
y=list(x)
y.remove("apple")
x=tuple(y)
print(x)

tuple=("dog","cat","eagle")
del tuple
print(tuple)






