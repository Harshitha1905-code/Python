#Create a list of 5 numbers and print the list.
num=[1,2,3,4,5]
print(num)

#2. Write a program to print the first and last element of a list.
num=[1,2,3,4,5]
print(num[0])
print(num[4])

#Write a program to find the length of a list.
a = [6,5,69 ,90,97,5]
print(len(a))

#Write a program to add an element at the end of a list.
fruits=['apple','banana','cherry']
fruits.append('mango')
print(fruits)

#Write a program to remove an element from a list
a = [3,4,8,0,90]
a.remove(0)
print(a)

#Write a program to reverse a list
num=[4,7,6,8,44]
num.reverse()
print(num)

#Write a program to find the largest number in a list.
num=[76,34,56,90,46]
print(max(num))

#Write a program to find the smallest number in a list.
num=[76,34,56,90,46]
print(min(num))

#Write a program to find the sum of all elements in a list.
num=[8,9,6,7,9,0]
print(sum(num))

#Write a program to count how many times a number appears in a list.
n=[1,2,3,2,4,2]
print(n.count(2))

#Write a program to sort a list in ascending order.
num=[90,66,88,99]
num.sort()
print(num)

#move zeros to end
num=[0,8,0,3,6]

non_zero=[x for x in num if x!=0]
zero=[0]*num.count(0)

result=non_zero+zero
print(result)




