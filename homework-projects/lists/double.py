def double(list:list[int]):
    new_list = [i+i for i in list]
    return new_list

def main():
    return double([1,2,3,4,5,6])

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    print(main())