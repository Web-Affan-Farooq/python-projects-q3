def divisors(num:int):
    ls = []
    for i in range(1,num+1):
        if(num%i == 0):
            ls.append(i)
        else: ""
    string = ""
    for item in ls:
        string += " "+str(item)
    return string

def main():
    user_input = input("Enter a number ")
    print(divisors(int(user_input)))

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()