def get_info(first_name, last_name, email):
    return first_name, last_name, email

def main():
    first_name = input("Enter your first name ")
    last_name = input("Enter your last name ")
    email = input("Enter your email")

    print(get_info(first_name,last_name,email))
    
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()