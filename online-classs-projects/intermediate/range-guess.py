import questionary
import random

points = 0
for i in range(5):
    num_for_comp = random.randint(1,100)
    num_for_human = random.randint(1,100)
    print(f"--------------Round-{i}----------------")
    user_input = questionary.confirm(message="Is your number is greater than computer or not ?").ask()
    if(user_input and num_for_human > num_for_comp):
        print("Great guess !")
        points +=1
    else :
        print("Wrong !")
    print(f"Points : {points}")
        
    