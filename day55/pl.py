lst = [1, 2, 2, 3, 3, 3, 4]
freq = {}
for i in lst:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

marks = {"a": 85, 
         "b": 92, 
         "c": 78
         }
max_subject = max(marks, key=marks.get)
print(max_subject)

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d1.update(d2)
print(d1)

d = {"a": 1, "b": 2, "c": 1}
inverted_d = {value: key for key, value in d.items()}
print(inverted_d)

#count characters in a string
s = "programming"
freq = {}
for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(freq)


