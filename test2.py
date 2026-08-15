#Knowledge Enhancement Alex has a list of books with reading times in array A, and N hours available. Determine the maximum number of books 
# he can read without exceeding his available hours. INPUT / OUTPUT input1: array A of reading times. input2: N hours available. input3: size of A.
#  Output: max books. EXAMPLE input1: [4,2,3,1] input2: 5 input3: 4 Output: 2
def max_books(A, N):
    A.sort()
    count = 0
    total_time = 0
    for time in A:
        if total_time + time <= N:
            total_time += time
            count += 1
        else:
            break
    return count
A=list(map(int,input().split()))
N=int(input())
size=int(input())
print(max_books(A, N))
