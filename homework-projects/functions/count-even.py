def count_even(num:int):
    ls = []
    ls.append(num)
    count = 0
    for item in ls:
        if(item%2 == 0):
            count+=1
        else : ""
    return count

def main():
    while(True):
        user_input= input("Enter an integer ")
        if(user_input != ""):
            print(count_even(int(user_input)))
        else : 
            print( "Exiting ...")
            break

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()