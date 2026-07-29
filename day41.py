#to find the index of a target number using linear search
arr=list(map(int,input("Enter the list of numbers separated by space: ").split()))
target=int(input())
for i in range(len(arr)):
    if arr[i]==target:
        print("The index of the target number is:",i)
        break
    else:
        print("The target number is not found in the list")    

#Write a Python program using Linear Search to count how many times a target element occurs in an array
arr = list(map(int, input().split()))
target = int(input())

count = 0

for i in range(len(arr)):
    if arr[i] == target:
        count += 1

print(count)   