#removes duplicates from a list
list=[1,2,2,2,3,3,4,4,5,5,5]
unique=set(list)#removes duplicates automatically
print(unique)

#Given a set {1, 2, 3, 4}, check if a number entered by the user exists.
set={1,2,3,4}
num=3
if num in set:
    print("present")
else:
    print("not present")    
 
s={1,2,3,44,55}
s.remove(44)
print(s)
s.discard(3)
print(s)

#Write a program to print the number of elements in a set.
set={22,33,44,55}
print(len(set))

#union of two sets
a={1,2,3}
b={4,5,6}
print(a|b)

#intersection of two sets
a={1,2,3}
b={2,3,4}
c=a.intersection(b)
print(c)

#difference between sets
a={1,2,3}
b={2,3,4}
print(a-b)

#symmetric difference
a={1,2,3}
b={2,3,4}
print(a^b)

#subset check
a={1,2}
b={1,2,3}
if a.issubset(b):
    print("a is subset ofa")
else:
    print("a is not subset of b")    
