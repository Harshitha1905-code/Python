#we can write quotes inside quotes
print('hi im "john"')
print("hi im 'john'")

#multiline string(3 quotes are used ' or "")
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt"""
print(a)

a= "Hello, World!"
print(a[1]) #it gives the second character of the string because indexing starts from 0

for x in "banana": #it gives each character of the string one by one
  print(x)

a = "Hello,World!"
print(len(a))  

txt= "The best things in life are free!"
print("free" in txt) #it gives true because "free" is present in the string

txt= "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt= "The best things in life are free!"
print("expensive" not in txt) #it gives true because "expensive" is


txt= "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

b = "Hello, World!"
print(b[2:5])   

b="Hello, World!"
print(b[:5]) #it gives the first 5 characters of the string

b="Hello,world"
print(b[4:]) #it gives the characters from index 4 to the end of the string

a="Hello, World!"
print(a[-5:-2]) #it gives the characters from index -5 to -2 (not including -2) of the string

s = "Computer"
print(s[-5:-1])

#print first 3 character of the string
s = "Computer"
print(s[:3])

#to extract middle character of the string
s = "Python"
print(s[len(s)//2])

s = "Python" #both start and end are omitted
#starting index default is 0 and ending index default is length of the string
print(s[:])

s = "Python"
print(s[4:2])
#The output is an empty string because the start index (4) is greater than the end index (2).



