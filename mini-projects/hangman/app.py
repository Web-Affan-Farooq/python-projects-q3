import random

# Number of mistakes allowed : 6
def draw_hangman(mistakes_count:int):
    if(mistakes_count == 0):
        print("  0  ")
        print(" /|\\ ")
        print(" / \\ ")
    elif(mistakes_count == 1):
        print("  0  ")
        print(" /|\\ ")
        print(" /  ")
    elif(mistakes_count == 2):
        print("  0  ")
        print(" /|\\ ")
        print(" ")
    elif(mistakes_count == 3):
        print("  0  ")
        print(" /| ")
        print(" ")
    elif(mistakes_count == 4):
        print("  0  ")
        print(" | ")
        print(" ")
    elif(mistakes_count == 5):
        print("  0  ")
        print(" ")
        print(" ")
    elif(mistakes_count == 6):
        print("Man is dead !")

def main(word:str):# kite
    messages = [
        "Hangman has only head left",
        "Hangman has only head and left hand left",
        "Hangman has only head and hands left",
        "Hangman has its head and left leg along with both hands left",
        "Hangman is safe",
        "Hangman is dead",
    ]
    chars = set(word) 
    lst = list(word)
    # print(f"Set : {chars}")
    # print(f"list : {lst}")
    # print(f"Newlist :{list(chars)}")
    count = len(word) # 3

    score = 0

    mistakes_count = 0

    constructed_string = []
    for char in chars:
        constructed_string.append("_")

    for char in chars : 
        print(constructed_string)
        char = char.lower()
        print(f"Required = {char}")
        user_guessed = input("Enter your guess  ").lower()
        idxs = []
        for i,item in enumerate(lst):
            if(item == char):
                idxs.append(i)
            else : pass

        if(user_guessed and len(user_guessed) != 0):
            if(user_guessed == char):
                print("Great ! you've guessed correct ")
                score +=1
                print(f"Score : {score}")
                # print(f"Total : {count}")

                for idx in idxs:
                    constructed_string[idx] = char 

            elif(user_guessed != char):
                print("Incorrect word ")
                if(score != 0):score-=1
                mistakes_count +=1
                print(f"Total : {count}")
                print(f"Mistakes : {mistakes_count}")
                print(f"Score : {score}")

            draw_hangman(mistakes_count)
        else :            
            print("Please enter only word") 
 
# List must contains word lengthen greater than or 6 
secret_words = [
    "Animal",
    "Kitten",
    "Dinosaur"
]
print("Caution : Only 6 incorrect guesses allowed ...")
selected_word = secret_words[random.randint(0,len(secret_words)-1)]

main(selected_word)