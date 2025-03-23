def subtract_seven(num:int):
    return num - 7

def main():
    user_input = input("Enter a number to subtract 7 ")
    print(subtract_seven(int(user_input)))

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()