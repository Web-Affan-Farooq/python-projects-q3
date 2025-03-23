def main():
    affirmation : str = "I am capable of doing anything I put my mind to."
    while(True):
        print(f"Please type this affirmation .. {affirmation}")
        user_input:str = input()
        if(user_input == affirmation):
            print("That's right ! ")
            break
        else : print("Incorrect affiramation ")
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()