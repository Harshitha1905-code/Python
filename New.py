def bubblesort(arr): 
    n = len(arr)#6
    
    for i in range(n): #i=6-->0,1,2,3,4
        for j in range(0, n-i-1): #6-3-1=2--->0,1
            if arr[j]>arr[j+1]: #5>3
                arr[j], arr[j+1] = arr[j+1], arr[j]#5-3
                
                    

    return arr
        
arr = list(map(int,input().split()))
print(bubblesort(arr))
