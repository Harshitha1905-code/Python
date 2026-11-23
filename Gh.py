#counting sort--------------

#arr = [3 3 2 4]

"""
def counting_sort(arr):

    max_val = max(arr)

    count = [0]*(max_val+1) #[0 0 1 2 1]
                            # 0 1 2 3 4

    for num in arr: #3 3 2 4
        count[num]+=1
    

    j= 0
    for i in range(len(count)): #0
        while count[i]>0:
            arr[j] = i
            j+=1
            count[i]-=1

    return arr
a = [8,6,4,9,1,2]
b= [3, 3, 2, 4]
print(counting_sort(a)) 
print(counting_sort(b))             

"""

#Stable counting sort--------------
#a = [3, 3, 2, 4]
"""
def count_sort(arr):

    max_val = max(arr)

    count = [0]*(max_val+1)#[0 0 0 0 0] = [0 0 1 2 1]

    #freq
    for num in arr:
        count[num]+=1

    #cumulative count

    for i in range(1, len(count)): #[0 0 1 3 4]
        count[i]+=count[i-1]

    output = [0]*len(arr)

    #right-left--

    for j in reversed(arr):
        output[count[j]-1] = j
        count[j]-=1

    return output


b= [3, 3, 2, 4]
a = [8,6,4,9,1,2]

print(count_sort(a))
print(count_sort(b)) 
"""
