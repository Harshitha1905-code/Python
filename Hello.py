def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

word = input("Enter a word or sentence: ")

if is_palindrome(word):
    print("Palindrome")
else:
    print("Not a palindrome")
