def double_int(count):
    return f"Double is {count + count}"

def main():
    user_input = int(input("Enter an integer "))
    print(double_int(user_input))
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()