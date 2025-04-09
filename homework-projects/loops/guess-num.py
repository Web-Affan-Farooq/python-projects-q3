import random
def main():
    print("-------------------- Guess my number --------------------")
    while(True):
        guessed = float(input("I am thinking of a number between 0 and 99... Enter a guess "))

        actual = random.randint(1,100)
        if(guessed > actual):
            print("Your guess is too high")
        elif(guessed < actual):
            print("Your guess is too low")
        elif(guessed == actual):
            print("Congrats ! You've guessed correct number ")
            break
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()