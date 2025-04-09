def main():
    user_input = input("What do you want? ")
    lst = []
    for item in user_input.split(" "):
        lst.append(item.lower())
    if("joke" in lst):
        print("Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'")
    else : 
        print("Sorry , I tell only joke")

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()