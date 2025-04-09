C = 299792458 

def main():
    m = float(input("Enter mass in kilograms "))
    e =  m * C**2
    return f"Total energy is {e:2f}"

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    print(main())