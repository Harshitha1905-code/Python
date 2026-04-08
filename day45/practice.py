lst=[1,2,2,3,4,4,5]
lt=[]
for i in lst:
    if i not in lt:
        lt.append(i)
print(lt)

#palindrome string
s="madam"
if s==s[::-1]:
    print("palindrome")
else:
    print("not palindrome")

s="hello world" 
dict={}
for char in s:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1
print(dict)  

#find the key with maximum value in a dictionary
dict={'a': 5, 'b': 3, 'c': 8}
max_key = max(dict, key=dict.get)
print("Key with maximum value:", max_key)

#find the key with minimum value in a dictionary
dict={'a': 5, 'b': 3, 'c': 8}
min_key = min(dict, key=dict.get)
print("Key with minimum value:", min_key)

#how to get  top two max values from a dictionary
dict={'a': 5, 'b': 3, 'c': 8}
