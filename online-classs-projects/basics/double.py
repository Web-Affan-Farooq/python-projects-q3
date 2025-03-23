def main():
    user_input = input("Enter a number ")
    count = 0
    while(True):
        num = int(user_input) + int(user_input)
        count += num
        if(count >= 100):
            break
        else : print(num)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()