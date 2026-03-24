thisset={"apple","banana","cherry"}
thisset.remove("banana")
print(thisset)

thisset={"apple","banana","cherry"}
thisset.discard("banana")
print(thisset)

set={"apple","banana","cherry"}
x=set.pop()
print(x)
print(set)

s={"apple","banana","cherry"}
s.clear()
print(s)

set={"mummy","daddy","sister"}
for x in set:
    print(x)

 #union method
set1={"mom","dad","sis"}
set2={1,2,3} 
set3=set1.union(set2)
print(set3)

set1={"mom","dad","sis"}
set2={1,2,3}
set3=set1|set2#| is union operator
print(set3)



