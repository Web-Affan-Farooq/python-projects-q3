import questionary
import random

choices = [
    "Rock",
    "Paper",
    "Scissor",
]
user_choice = questionary.select(choices=choices, message="Select choice ").ask()
random_choice = choices[random.randint(0,2)]

if(user_choice == random_choice):
    print("Match is tied ..")
    print(f"Your choice : {user_choice} ")
    print(f"opponent : {random_choice} ") 
elif(user_choice == "Rock" and random_choice == "Scissor"):
    print("Conguratulations ! you've won the match ")
    print(f"Your choice : {user_choice} ")
    print(f"opponent : {random_choice} ") 
elif(user_choice == "Scissor" and random_choice == "Paper"):
    print("Conguratulations ! you've won the match ")
    print(f"Your choice : {user_choice} ")
    print(f"opponent : {random_choice} ") 
elif(user_choice == "Paper" and random_choice == "Rock"):
    print("Conguratulations ! you've won the match ")
    print(f"Your choice : {user_choice} ")
    print(f"opponent : {random_choice} ") 
else:
    print("You've loss the match .")
    print(f"Your choice : {user_choice} ")
    print(f"opponent : {random_choice} ") 