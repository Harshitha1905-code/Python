#Write a program to check whether a given string starts with "A".
string = "Apple"
if string.startswith("A"):
    print("The string starts with 'A'.")

#Write a program to replace a word in a sentence.
sentence = "I like cats."
new_sentence = sentence.replace("cats", "dogs")
print(new_sentence)

#Write a program to reverse a string.
string = "Hello, World!"
reversed_string = string[::-1]
print(reversed_string)

#Write a program to print every second character in a string.
string = "Hello, World!"
every_second_char = string[::2]
print(every_second_char)

#Write a program to check whether a number is greater than 50 and print True or False.
number = 75
if number > 50:
    print(True)
else:
    print(False)

#Write a program to check whether a number is even using boolean expression.
number = 10
if number % 2 == 0:
    print(True)
else:
    print(False)

# Write a program to check whether two numbers are equal.
num1=5
num2=5
if num1 == num2:
    print(True)
else:
    print(False)

# Write a program that checks if a string is empty and returns True or False.
string = ""
if string == "":
    print(True)
else:    print(False)

#Write a program to check whether a number is positive, negative, or zero.
number = -5
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

 #Write a program to check whether a number is divisible by both 3 and 5.
number=15
if number%3==0 & number%5==0:
    print("Divisible by both 3 and 5")
else:
    print("Not Divisible by 3 and 5")  

 
    