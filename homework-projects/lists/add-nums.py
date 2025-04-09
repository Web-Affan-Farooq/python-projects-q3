def add(list:list[int]):
    sum = 0;
    for i in list:
        sum +=i
    return f"Sum on numbers is {sum}"

def main():
    return add([1,2,3,4,5,6])

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    print(main())