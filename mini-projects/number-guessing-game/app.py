import questionary
import random 

def easy_game():
    while (True):
        user_input = int(input("Enter number to guess between 1 to 5 "))
        required_num = random.randint(1,5)
        
        if(user_input == required_num):
            print("Conguratulations ! You guessed correct number. ")
            break
        elif(user_input == ""):
            print("Please enter a correct number without floating points ")
        else:
            print("You guessed wrong ")

def medium_game():
    while (True):
        user_input = int(input("Enter number to guess between 1 to 10 "))
        required_num = random.randint(1,10)
        
        if(user_input == required_num):
            print("Conguratulations ! You guessed correct number. ")
            break
        elif(user_input == ""):
            print("Please enter a correct number without floating points ")
        else:
            print("You guessed wrong ")

def hard_game():
    while (True):
        user_input = int(input("Enter number to guess between 1 to 20 "))
        required_num = random.randint(1,20)
        
        if(user_input == required_num):
            print("Conguratulations ! You guessed correct number. ")
            break
        elif(user_input == ""):
            print("Please enter a correct number without floating points ")
        else:
            print("You guessed wrong ")

options = [
        "Easy",
        "Medium",
        "Hard",
    ]
difficulty = questionary.select(choices=options, message="Select difficulty ").ask()

if(difficulty == "Easy"):
    easy_game()
elif(difficulty == "Medium"):
    medium_game()
elif(difficulty == "Hard"):
    hard_game()