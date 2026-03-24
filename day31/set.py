#join multiple sets
set1={"a","b","c"}
set2={1,2,3}
set3={"apple","banana","cherry"}
set4={"John","Elena"}
#set5=set1.union(set2,set3,set4)
set5=set1|set2|set3|set4
print(set5)

#join a set and tuple
x={"a","b","c"}
y=(1,2,3)
z=x.union(y)
print(z)

#update method
set1={"a","b","c"}
set2={1,2,3}
set1.update(set2)
print(set1)

#intersection
set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
#set3=set1.intersection(set2)
set3=set1&set2
print(set3)

set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set1.intersection_update(set2)
print(set1)

set1={"apple",True,"banana",0,"cherry"}
set2={False,"google",1,"apple",2}
set3=set1.intersection(set2)
print(set3)



