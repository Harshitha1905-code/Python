#Red Pen Green Pen 
# You write N numbers on a whiteboard using a green pen for odd numbers and a red pen for even numbers. Return the number of times you switch
#  from the green pen to the red pen. INPUT / OUTPUT input1: N. input2: array of numbers. Output: number of green-to-red switches. 
# EXAMPLE input1: 5 input2: {1,2,1,6,10,9} Output: 2 input1: 6 input2: {70,23,13,26,72,19} Output: 1
#odd number->green pen, even number->red pen
#we need to count only Green->Red switches
#so,whenever an odd number is followed by an even number, we increment the count
n = int(input())
arr = list(map(int, input().split()))
count = 0
for i in range(1, n):
    if arr[i-1] % 2 != 0 and arr[i] % 2 == 0:
        count += 1
print(count)

