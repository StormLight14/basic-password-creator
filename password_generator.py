import random                                           
import string                                           
password_chars = string.printable[:-len(string.whitespace)]                                                     
password = ""
try:
    password_length = int(input("Please enter a password length: "))
    for num in range(password_length):
        password += random.choice(password_chars)
    print(password)
except ValueError:
    print("Please enter a whole number.")
