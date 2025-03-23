def greetings(name:str):
    return f"Have a good day {name}"
def main():
    user_input = input("Enter your name ")
    print(greetings(user_input))

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()