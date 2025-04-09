def check_odd(num):
    if(num%2 != 0):
        return True
    else : return False
def main():
    for i in range(0,20):
        if(check_odd(i)):
            print(f"Number {i} is odd")
        else : print(f"Number {i} is even")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()