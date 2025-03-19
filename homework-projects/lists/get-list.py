def main():
    ls = []
    while True:
        str = input("Please enter list item ")
        if(str != ""):
            ls.append(str)
        else : 
            print(f"Here is the list : {ls}")
            break

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()