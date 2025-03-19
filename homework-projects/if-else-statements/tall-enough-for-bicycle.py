def main():
    while True:
        length =  int(input("Enter Your height "))
        if (length > 0 and not None):
            if(length >= 50):
                print("You're tall enough to ride a bicycle")
            else : print("You're not tall enough to ride bicycle")
        else :
           print( "Exit ..")
           break           

if __name__ == '__main__':
    main()
