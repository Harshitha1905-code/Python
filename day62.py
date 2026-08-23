#Missing Number Given an array of numbers from 1 to n with one missing, find the missing number.
arr=list(map(int,input().split()))
n=len(arr)+1#to find which number is missing we need to know len(arr)+1
total_sum=n*(n+1)//2 #sum of numbers from 1 to n
missing=total_sum-sum(arr) #calculate the missing number
print(missing)




