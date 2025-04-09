import random

def return_str(count: int, condition=False):
    string = str(count)

    if condition:
        return f"I'm going to count until 10 or until I feel like stopping, whichever comes first. {string}. I am done."
    else:
        return f"I'm going to count until 10 or until I feel like stopping, whichever comes first. {string}"

def I_am_done():
    randInt = random.randint(1, 10)
    luckyNum = 7
    return luckyNum == randInt  

def count_function():
    for i in range(1, 11):  
        if I_am_done(): 
            print(return_str(i, True))
            return
        else:
            print(return_str(i))
def main():
    count_function()

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
