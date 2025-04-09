def main():
    year = int(input("Enter year to be checked "))
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("It's leap year ")
    else :
        print("It's not leap year ")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()