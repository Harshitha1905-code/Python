#difference sets
set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
#set3=set1.difference(set2)
set3=set1-set2
set3=set2-set1
print(set3)

set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set1.difference_update(set2)
print(set1)

#symmetric difference
set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set3=set1.symmetric_difference(set2)
print(set3)

set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set3=set1^set2
print(set3)

set1={"apple","banana","cherry"}
set2={"google","microsoft","apple"}
set1.symmetric_difference_update(set2)
print(set3)

#frozen set
x=frozenset({"apple","banana","cherry"})
print(x)
print(type(x))