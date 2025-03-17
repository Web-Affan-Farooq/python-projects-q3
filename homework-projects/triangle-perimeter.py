def main():
    side_1 = input("What is the length of side 1 ? ")
    side_2 = input("What is the length of side 2 ? ")
    side_3 = input("What is the length of side 3 ? ")

    print(f"The Perimeter of triangle is {float(side_1)+float(side_2)+float(side_3)}")
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()