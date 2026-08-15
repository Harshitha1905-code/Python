#Minimum Sum Test
#Problem: You are given two integer arrays A and B of length N on which you have to perform below operation: In one operation, you can swap any 
# two elements of 'A' or any two elements of 'B'Consulting
#Your task is to find and return an integer value representing the minimum possible sum of A[i]*B[i] after performing the above operation any 
# number of times. 
# Note: The operation can also be performed 0 number of times.
#Input Specification:
#input1: An integer value N representing the size of arrays.
#input2: An integer array A
#input3: An integer array B
#Output Specification: Return an integer value representing the minimum possible sum of A[i]*B[i] after performing the above operation any 
# number of times.
#Example 1:
#input1: 4
#input2: {1,4,1,6}
#input3: {1,4,3,4}
#Output: 25
#Explanation: Here A = {1,4,3,2} and B = {1,4,3,4}. To minimize the sum, we can swap the first two elements of A i.e.,
#  4 and 1. The array will now become (4,1,3,2). The sum obtained will be 25, which is the minimum. Hence, 25 is returned as the output.
def minSum(N, A, B):
    A.sort()#ascending order
    B.sort(reverse=True)#descending order
    total_sum = 0
    for i in range(len(A)):
        total_sum += A[i] * B[i]
    return total_sum
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
print(minSum(N, A, B))

