import questionary
from hashlib import sha256
import os

book :dict = {
        "example@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8", # word
        "code_in_placer@cip.org": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc", # karel
        "student@stanford.edu": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb" # password
        }

options = [
    "Add new",
    "Find ",
    "Exit",
]
while True:
    print(book)
    choice = questionary.select(choices=options, message="Select option").ask()
    if(choice == options[0]):
        password = questionary.text("Enter password ").ask()
        credential = questionary.text("From which credential it belongs to (www.exampleweb.io)").ask()
        book[credential] = sha256(password.encode()).hexdigest()

    elif(choice == options[2]):
        os._exit(0)
    elif(choice == options[1]):
        password = questionary.text("Enter password ").ask()
        credential = questionary.text("From which credential it belongs to (www.exampleweb.io)").ask()
        required = {}
        for item in book.keys():
            if(item == credential):
                print(f"{password} belongs to {credential}")