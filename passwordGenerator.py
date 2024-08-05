import random
import string
import pyperclip

while True:
    try:
        length2=length=int(input("Enter the length of the password: "))
        if(length<8):
            print("Minimum length is 8")
            continue
        break
    except ValueError:
        print("Enter valid integer")

print("Enter your choice: ")
upperCase=input("Enter 'yes' to add uppercase letters: ").strip().lower()
lowerCase=input("Enter 'yes' to add lowercase letters: ").strip().lower()
digits=input("Enter 'yes' to add digits: ").strip().lower()
punctuation=input("Enter 'yes' to add special symbols: ").strip().lower()

generatedPassword=""

while length>0:
    if(upperCase=='yes'):
        generatedPassword+=random.choice(list(string.ascii_uppercase))
        length-=1
    if(lowerCase=='yes'):
        generatedPassword+=random.choice(list(string.ascii_lowercase))
        length-=1
    if(digits=='yes'):
        generatedPassword+=random.choice(list(string.digits))
        length -= 1
    if(punctuation=='yes'):
        generatedPassword+=random.choice(list(string.punctuation))
        length -= 1

if not generatedPassword:
    print("No character types selected")

# print(generatedPassword)
password=""
for i in range(length2):
    password+=random.choice(list(generatedPassword))
print(f"Your password is: {password}")

pyperclip.copy(password)
print("Password copied to clipboard")