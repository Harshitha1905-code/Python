#Write a program to check whether a given string starts with "A"
string = "Apple"
if string.startswith("A"):
    print("The string starts with 'A'")

# Write a program to replace a word in a sentence.
sentence = "I like cats"   
new_sentence=sentence.replace("cats","dogs")
print(new_sentence)

#Write a program to reverse a string.
string = "Hello, World!"
reversed_string = string[::-1]
print(reversed_string)

#Given a string "PYTHONPROGRAM", print:
#First 6 characters
#Last 5 characters
#Characters from index 2 to 8
string = "PYTHONPROGRAM"
print(string[:6])  # First 6 characters
print(string[-5:])  # Last 5 characters
print(string[2:9])  # Characters from index 2 to 8

#Write a program to print every second character in a string.
string = "Hello, World!"
print(string[::2])

#Write a program to remove the first and last characters of a string.
string = "Hello, World!"
new_string = string[1:-1]
print(new_string)

#rite a program to print the string in reverse using slicing.
string = "Hello, World!"
reversed_string = string[::-1]
print(reversed_string)



