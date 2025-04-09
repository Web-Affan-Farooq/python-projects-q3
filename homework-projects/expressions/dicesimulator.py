import random

def main():
    random_num_1 = random.randint(1,6)
    random_num_2 = random.randint(1,6)
    return random_num_1 + random_num_2

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    print("dice starts as 10")
    print(main())
    print(main())
    print(main())
    print("dice stops as 10")
