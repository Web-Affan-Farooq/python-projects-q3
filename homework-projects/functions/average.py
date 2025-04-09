def average():
    num_1 = int(input("Enter first number "))
    num_2 = int(input("Enter second number "))
    return print(f"Average is {(num_1 + num_2) / 2 }")

def main():
    average()
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()