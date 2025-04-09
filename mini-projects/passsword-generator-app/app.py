# Create a prompt for password length (10 character , 20  , 30 0r 40 )
import questionary
import string
import random

def generate_password(length:int):
    chars = list(string.ascii_uppercase) + list(string.ascii_lowercase) + list(string.digits) + list('!@#$%^&*()-_=+[]{};:\'",.<>?/\\|`~')
    
    text = []
    password = ""
    for i in range(length + 1):
        text.append(random.choice(chars))
    
    for item in text:
        password += item

    return print(password)        
    
options = [
    "10 characters",
    "20 characters",
    "30 characters",
    "40 characters",
]
length = questionary.select(choices=options, message="Select password length").ask()

if(length == options[0]):
    generate_password(10)
elif(length == options[1]):
    generate_password(20)
elif(length == options[2]):
    generate_password(30)
elif(length == options[3]):
    generate_password(40)