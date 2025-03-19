def main():
    ls = []
    while True:
        name = input("Please enter name of recipent  ")
        phone_number = input("Enter phonenumber  ")
        print(f"\n")
        print(f"\n")
        if(name != "" and phone_number != ""):
            ls.append({"Name":name,"PhoneNumber":phone_number})
            print("Your phone book :  --------------------")
            print(f"\n")
            for item in ls:
                print(f"Name : {item["Name"]}    ;    Phonenumber : {item["PhoneNumber"]}")
                print(f"\n")
        else :
            print("Exit ...")
            break
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()