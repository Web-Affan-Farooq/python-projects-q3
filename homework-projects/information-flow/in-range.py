def in_range(num:int):
    return num in range(1,11)
def main():
    user_input = int(input("Enter integer "))
    print(in_range(user_input))

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()