a="Hello"
print(a.upper())

a="Hello"
print(a.lower())

a="Hello, World!"
print(a.strip()) #it removes any whitespace from the beginning or the end of the string

a="Hello, World!"
print(a.replace("H", "J")) #it replaces all the occurrences of "H" with "J"

a="Hello, World!"
print(a.split(",")) #it splits the string into a list where each word is a list

a="Hello"
b="World"
c=a + " " + b #it concatenates the two strings with a space in between
print(c)

age=36
txt=f"My name is John, and I am {age}"
print(txt)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

txt="We are the so-called \"Vikings\" from the north."
print(txt)


