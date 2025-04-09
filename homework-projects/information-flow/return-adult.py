MAX_ADULT = 35
def is_adult(num:int):
    if(num >= MAX_ADULT):
        return True
    elif(num <MAX_ADULT):
        return False
def main():
    user_input = int(input("Enter age of the person "))
    print(is_adult(user_input)) 
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()