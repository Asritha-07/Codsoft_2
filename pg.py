#password generator
import random
import string
password_length=int(input("Enter any length:"))
def password_generator(length=password_length, use_uppercase=True, use_digits=True, use_punctuation=True):
       characters = string.ascii_lowercase
       if use_uppercase:
           characters += string.ascii_uppercase
       if use_digits:
           characters += string.digits
       if use_punctuation:
           characters += string.punctuation

       password = ''.join(random.choices(characters,k=length))
       print(f"Generated password: {password}")

password_generator()