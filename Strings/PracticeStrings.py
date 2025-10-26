name = "Abdul Samad"
print(name[0])
print(name[-1])
print(len(name))
s1="Hello"
s2="World"
print(s1+" "+s2)
print(s1,s2)

text = "Python Programming"
print(text[0:6])
print(text[-6:])
print(text[::2])
print(text[::-1])

func=" i love python programming "
print(func)
print(func.strip())
print(func.title())
print(func.count("o"))
str4= "abc"
print(str4.isalpha())
print(str4.isalnum())
name="John"
age=25
print(f"My name is {name} and I am {age} years old.")
sentence="Coding in Python is fun"
print(sentence.replace("fun", "awesome"))
print(sentence.index("Python"))
print(sentence.upper())

sentence=input("Enter a string: ")
sum=0
vowels = ['a', 'e', 'i', 'o', 'u']
for char in sentence.lower():
    #print(char)
    if char in vowels:
        sum += 1
print("Number of vowels:", sum) 

word=input("Enter a word: ")
if word.lower()==word[::-1].lower():
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")   