import random

def roll_dice():
    random_num_1 = random.randint(1, 6)  
    random_num_2 = random.randint(1, 6)
    total = random_num_1 + random_num_2  
    print(f"Die 1: {random_num_1}, Die 2: {random_num_2} , Total: {total}")

def main():
    print("Rolling the dice...")
    for _ in range(3):
        roll_dice()
    print("Dice rolling finished.")


if __name__ == '__main__':
    main()
