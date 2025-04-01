import questionary
import random
import math

# def hangman(score: int, total: int):
#     # Calculate threshold for each stage
#     calculated = total / 5  # Divide total mistakes into 5 equal parts
    
#     messages = [
#         "Hangman has only head left",
#         "Hangman has only head and left hand left",
#         "Hangman has only head and hands left",
#         "Hangman has its head and left leg along with both hands left",
#         "Hangman is safe",
#         "Hangman is dead",
#     ]

#     if score <= 0:  # If score is 0 or negative, Hangman is dead
#         return messages[5]
#     elif score <= calculated * 1:
#         return messages[0]
#     elif score <= calculated * 2:
#         return messages[1]
#     elif score <= calculated * 3:
#         return messages[2]
#     elif score <= calculated * 4:
#         return messages[3]
#     else:
#         return messages[4]  # Score is high enough, Hangman is safe
def hangman(mistakes_count:int, total:int):
    calculated = total // 5
    messages = [
        "Hangman has only head left",
        "Hangman has only head and left hand left",
        "Hangman has only head and hands left",
        "Hangman has its head and left leg along with both hands left",
        "Hangman is safe",
        "Hangman is dead",
    ]
    if mistakes_count >= total:  # Too many mistakes, Hangman is dead
        print(messages[5])
    elif mistakes_count >= calculated * 4:
        print(messages[4])
    elif mistakes_count >= calculated * 3:
        print(messages[3])
    elif mistakes_count >= calculated * 2:
        print(messages[2])
    elif mistakes_count >= calculated * 1:
        print(messages[1])
    else:
        print(messages[0])
    
    # ___find any logical error 

def main(word:str):# kite
    messages = [
        "Hangman has only head left",
        "Hangman has only head and left hand left",
        "Hangman has only head and hands left",
        "Hangman has its head and left leg along with both hands left",
        "Hangman is safe",
        "Hangman is dead",
    ]
    count = len(word) # 3
    score = 0
    mistakes_count = 0
    for i in range(count):
        required = word[i].lower()
        print(f"Required = {required}")
        user_guessed = input("Enter your guess  ").lower() 
        if(user_guessed):
            if(user_guessed == required):
                print("Great ! you've guessed correct ")
                print(f"Score : {score}")
                print(f"Total : {count}")

            elif(user_guessed != required):
                print("Incorrect word ")
                print(f"Score : {score}")
                print(f"Total : {count}")
                mistakes_count +=1
                hangman(mistakes_count, count)
        else :            
            print("Please enter a word")
        # calculated = count - count / 5
        # print(f"Required : {required}")
        # if(user_guessed != "" and user_guessed == required):
        #     print("Great guess ")
        #     score+=1 # score = 1
        #     print("Score : ", score)
        #     print("Total : ",count )
        #     if(score >= 0 and score <= int(count / 5)*1):
        #         print(messages[0])
        #     elif(score > int(count/5)*1 and score <= int(count / 5)*2):
        #         print(messages[1])
        #     elif(score > int(count/5)*2 and score <= int(count / 5)*3):
        #         print(messages[2])
        #     elif(score > int(count/5)*3 and score == int(count / 5)*4):
        #         print(messages[3])
        #     elif(score > int(count/5)*4 and score == int(count / 5) *5):
        #         print(messages[4])                
        #     elif(score <=0):
        #         print(messages[5])
        # elif(user_guessed != "" and user_guessed != required):
        #     print(f"Wrong ! the word is {required}")
        #     score-=1 # score = 1
        #     print("Score : ", score)
        #     print("Total : ",count )
        #     if(score >= 0 and score <= int(count / 5)*1):
        #         print(messages[0])
        #     elif(score > int(count/5)*1 and score <= int(count / 5)*2):
        #         print(messages[1])
        #     elif(score > int(count/5)*2 and score <= int(count / 5)*3):
        #         print(messages[2])
        #     elif(score > int(count/5)*3 and score == int(count / 5)*4):
        #         print(messages[3])
        #     elif(score > int(count/5)*4 and score == int(count / 5) *5):
        #         print(messages[4])                
        #     elif(score <=0):
        #         print(messages[5])

    
secret_words = [
    "Animal",
    "kite",
    "cat"
]

selected_word = secret_words[random.randint(0,len(secret_words)-1)]

main(selected_word)
