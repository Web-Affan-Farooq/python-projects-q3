def main():
    dictionary = {
        "Apple":5,
        "Banana":5,
        "Mango":10,
    }
    total = 0
    for item in dictionary:
        ans = int(input(f"How many {item}s you want "))
        if (ans != None):
            amount = ans * dictionary[item]
            total += amount
        else :
            print("Please enter a digit ")
            continue
    
    print(f"Total amount : {total}")
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()