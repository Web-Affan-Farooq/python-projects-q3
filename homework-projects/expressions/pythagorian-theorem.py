import math
def main():
    side_a = float(input("Enter length of first perpendicular side of triangle"))
    side_b = float(input("Enter length of second perpendicular side of triangle"))
    c = math.sqrt(side_a**2 + side_b**2) 
    return f"The length of hypotenuse of \n A = {side_a} and \n B = {side_b} \n is {c:.2f}"

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    print(main())