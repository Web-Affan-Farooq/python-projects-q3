def shorten(ls:list):
    ls.pop(-1)
    return ls

def main():
    ls = ["Hello 1","Hello 2", "Hello 3", "Hello 4"]
    return shorten(ls)
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    print(main())