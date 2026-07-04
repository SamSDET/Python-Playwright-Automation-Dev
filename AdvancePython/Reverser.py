text = input("Enter a text: ")
lowertext = text.lower()
reversed_text = "".join(reversed(lowertext))
print(reversed_text)

if lowertext == reversed_text:
    print("The text is a palindrome.")
else:
    print("The text is not a palindrome.")