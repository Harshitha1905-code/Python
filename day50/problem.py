#Medium level
#Find the subject with the highest marks.
marks = {
    "Maths": 85,    
    "Science": 90,
    "English": 80,
}
max_subject = max(marks, key=marks.get)
print(max_subject)

#Count frequency of elements in a list using a dictionary:
lst=[1,2,2,3,3,3,4]
freq={}
for i in lst:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)

#Merge two dictionaries:
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1)

#Create a dictionary from two lists:
keys = ["a", "b", "c"]
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
print(my_dict)

#Invert a dictionary (swap keys and values):
my_dict = {"a": 1, "b": 2, "c": 3}
inverted_dict = {value: key for key, value in my_dict.items()}
print(inverted_dict)

#find the number that appears the most times
nums = [1, 3, 2, 1, 4, 1, 3, 3, 3]
freq = {}
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
most_frequent_num = max(freq, key=freq.get)
print(most_frequent_num)

#Find the second most frequent element in:
nums = [4, 4, 2, 2, 2, 3, 3, 3, 3, 1]
freq={}
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
second_most_frequent_num = sorted_freq[1][0]    
print(second_most_frequent_num)