def main():
    num_1 = float(input("Please enter an integer to be divided "))
    num_2 = float(input("Please enter an integer to divide by "))
    if(num_2 != 0):
         return f"Result : {num_1/num_2} , Remainder : {num_1 % num_2}"
    else : return "Error ! No zeros are allowed in denominator"
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    print(main())